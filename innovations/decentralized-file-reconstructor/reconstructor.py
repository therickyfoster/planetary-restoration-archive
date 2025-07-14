#!/usr/bin/env python3
# reconstructor.py — AI-Driven Decentralized File Reconstructor (Master Edition)

import os
import sys
import argparse
import hashlib
import requests
import tempfile
import shutil
from pathlib import Path
from typing import Generator, Optional

from agents.agent_orchestrator import AgentOrchestrator
from utils.chunk_utils import chunk_hash, verify_chunk_integrity
from utils.ipfs_client import fetch_chunk_from_ipfs
from utils.output_writer import OutputWriter
from config.system_config import RAM_CAP_MB

# Initialize AI agent logic
orchestrator = AgentOrchestrator()

class ChunkStreamManager:
    def __init__(self, source: str, mode: str = "auto"):
        self.source = source
        self.mode = mode
        self.chunk_size = 5 * 1024 * 1024  # 5MB default
        self.temp_dir = tempfile.mkdtemp()
        self.is_ipfs = source.startswith("Qm") or source.startswith("bafy")

    def stream_chunks(self) -> Generator[tuple[bytes, str], None, None]:
        if self.is_ipfs:
            print(f"[INFO] Pulling from IPFS: {self.source}")
            index = 0
            while True:
                try:
                    chunk = fetch_chunk_from_ipfs(self.source, index)
                    if not chunk:
                        break
                    chunk_hash_id = chunk_hash(chunk)
                    yield chunk, chunk_hash_id
                    index += 1
                except Exception as e:
                    print(f"[WARN] Failed to fetch chunk {index}: {e}")
                    break
        else:
            print(f"[INFO] Local file detected: {self.source}")
            with open(self.source, "rb") as f:
                while chunk := f.read(self.chunk_size):
                    chunk_hash_id = chunk_hash(chunk)
                    yield chunk, chunk_hash_id

    def cleanup(self):
        shutil.rmtree(self.temp_dir)

def reconstruct_file(source: str, output_dir: str, mode: str = "auto"):
    stream_manager = ChunkStreamManager(source, mode)
    writer = OutputWriter(output_dir)
    reconstructed_count = 0

    for chunk, hash_id in stream_manager.stream_chunks():
        try:
            if not verify_chunk_integrity(chunk, hash_id):
                print(f"[ERROR] Integrity mismatch: {hash_id}")
                continue

            result = orchestrator.process_chunk(chunk, hash_id)
            if result:
                writer.write_result(result, hash_id)
                reconstructed_count += 1
            else:
                print(f"[WARN] No output from AI pipeline for chunk {hash_id}")
        except Exception as e:
            print(f"[FAIL] Chunk {hash_id} failed: {e}")
            continue

    writer.finalize()
    stream_manager.cleanup()
    print(f"[DONE] Reconstruction complete. {reconstructed_count} chunks processed.")

def cli():
    parser = argparse.ArgumentParser(description="AI-Based File Reconstructor")
    parser.add_argument("--input", required=True, help="Path to file or IPFS CID")
    parser.add_argument("--output", default="./reconstructed/", help="Output directory")
    parser.add_argument("--mode", default="auto", help="Reconstruction mode (auto/binary/media/text)")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    reconstruct_file(args.input, args.output, args.mode)

if __name__ == "__main__":
    cli()
