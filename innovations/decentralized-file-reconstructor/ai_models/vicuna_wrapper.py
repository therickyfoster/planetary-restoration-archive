# ai_models/vicuna_wrapper.py
# Uses Vicuna LLM to reconstruct or interpret chunked content

import subprocess
import requests

# Endpoint for local Ollama instance running Vicuna or any LLM API
VICUNA_ENDPOINT = "http://localhost:11434/api/generate"

def complete_with_vicuna(chunk: bytes, model: str = "vicuna") -> bytes:
    """
    Sends a chunk to Vicuna for semantic reconstruction or extension.
    """
    try:
        prompt = chunk.decode("utf-8", errors="ignore")
        if not prompt.strip():
            return b""

        payload = {
            "model": model,
            "prompt": f"You are a file reconstruction AI. Complete or repair the following input segment:\n\n{prompt}",
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.95,
                "max_tokens": 512
            }
        }

        response = requests.post(VICUNA_ENDPOINT, json=payload, timeout=15)
        response.raise_for_status()

        result = response.json().get("response", "").strip()
        return result.encode("utf-8")

    except Exception as e:
        print(f"[VICUNA ERROR] {e}")
        return b"[ERROR]"
