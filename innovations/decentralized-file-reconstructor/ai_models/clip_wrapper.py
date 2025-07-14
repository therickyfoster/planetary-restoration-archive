# ai_models/clip_wrapper.py
# Embeds file chunks using CLIP for semantic routing and AI context seeding

import io
import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

# Load once, shared across system
model_name = "openai/clip-vit-base-patch32"
clip_model = CLIPModel.from_pretrained(model_name)
clip_processor = CLIPProcessor.from_pretrained(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
clip_model.to(device)

def embed_clip(chunk: bytes) -> str:
    """
    Accepts a chunk (image or image-like binary), converts to tensor, and returns semantic embedding.
    For now, returns top text tokens, could later route full vector.
    """
    try:
        image = Image.open(io.BytesIO(chunk)).convert("RGB")
        inputs = clip_processor(images=image, return_tensors="pt").to(device)
        outputs = clip_model.get_text_features(**inputs)
        keywords = outputs.cpu().detach().numpy().tolist()[0][:8]  # Take first 8 values
        return "clip:" + ",".join([f"{round(val, 4)}" for val in keywords])
    except Exception as e:
        print(f"[CLIP ERROR] {e}")
        return "clip:unreadable"
