# utils/chunk_utils.py
# Utility functions for hashing and verifying file chunks

import hashlib

def chunk_hash(chunk: bytes, algo: str = "sha256") -> str:
    """
    Computes a unique hash for a given chunk using the specified algorithm.
    """
    h = hashlib.new(algo)
    h.update(chunk)
    return h.hexdigest()

def verify_chunk_integrity(chunk: bytes, expected_hash: str, algo: str = "sha256") -> bool:
    """
    Verifies a chunk’s integrity by comparing its hash to the expected value.
    """
    calculated_hash = chunk_hash(chunk, algo)
    if calculated_hash != expected_hash:
        print(f"[INTEGRITY ERROR
