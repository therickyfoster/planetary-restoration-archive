# ai_models/t5_fallback.py
# Lightweight fallback reconstruction using T5

from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# Load model once
model_name = "t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def complete_with_t5(input_data: bytes) -> bytes:
    """
    Attempts to reconstruct or summarize the input using T5.
    Returns a completed text segment as bytes.
    """
    try:
        text = input_data.decode("utf-8", errors="ignore")
        if not text.strip():
            return b""

        prompt = f"repair or complete the following: {text}"
        input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
        output_ids = model.generate(input_ids, max_length=256, num_beams=4, early_stopping=True)

        output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        return output.encode("utf-8")

    except Exception as e:
        print(f"[T5 ERROR] {e}")
        return b""
