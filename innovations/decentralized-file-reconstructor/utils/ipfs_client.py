# utils/ipfs_client.py
# IPFS integration for chunk-based streaming and retrieval

import requests
import base64

IPFS_GATEWAYS = [
    "https://ipfs.io/ipfs/",
    "https://cloudflare-ipfs.com/ipfs/",
    "https://gateway.pinata.cloud/ipfs/"
]

CHUNK_SUFFIX_TEMPLATE = "?chunk={}"  # Extend if needed for pinning services

def fetch_chunk_from_ipfs(cid: str, index: int, max_size: int = 5 * 1024 * 1024) -> bytes:
    """
    Attempts to fetch a chunk from a decentralized IPFS CID with retries across gateways.
    """
    suffix = CHUNK_SUFFIX_TEMPLATE.format(index)
    for gateway in IPFS_GATEWAYS:
        url = f"{gateway}{cid}{suffix}"
        try:
            print(f"[IPFS] Fetching chunk {index} from: {url}")
            response = requests.get(url, timeout=10)
            if response.status_code == 200 and response.content:
                return response.content[:max_size]
        except Exception as e:
            print(f"[WARN] Failed from {gateway}: {e}")
    raise RuntimeError(f"All gateways failed for chunk index {index}")

def encode_chunk_to_base64(chunk: bytes) -> str:
    return base64.b64encode(chunk).decode("utf-8")

def decode_chunk_from_base64(encoded: str) -> bytes:
    return base64.b64decode(encoded.encode("utf-8"))
