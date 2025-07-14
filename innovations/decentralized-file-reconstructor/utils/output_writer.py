# utils/output_writer.py
# Manages output reconstruction and hash-indexed writing to disk

import os
import hashlib
from pathlib import Path

class OutputWriter:
    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.chunk_log = self.output_dir / "reconstruction.log"
        self.seen_hashes = set()

        # Resume support
        if self.chunk_log.exists():
            with open(self.chunk_log, "r") as log:
                for line in log:
                    self.seen_hashes.add(line.strip())

    def write_result(self, content: bytes, hash_id: str):
        """
        Writes a reconstructed chunk to disk using its hash as filename.
        Appends to the reconstruction log for resume capability.
        """
        if hash_id in self.seen_hashes:
            print(f"[SKIP] Already reconstructed: {hash_id}")
            return

        filename = self.output_dir / f"{hash_id}.chunk"
        with open(filename, "wb") as f:
            f.write(content)

        with open(self.chunk_log, "a") as log:
            log.write(f"{hash_id}\n")

        self.seen_hashes.add(hash_id)
        print(f"[WRITE] {filename}")

    def finalize(self):
        """
        Optional post-processing hook. Could stitch binary files,
        merge text segments, or trigger transcoding.
        """
        print(f"[DONE] Output stored in: {self.output_dir.resolve()}")
