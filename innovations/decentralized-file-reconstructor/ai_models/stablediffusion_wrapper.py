# ai_models/stablediffusion_wrapper.py
# Visual reconstruction and enhancement using Stable Diffusion

import io
import torch
from PIL import Image
from diffusers import StableDiffusionImg2ImgPipeline

# Load the pipeline (can be customized per device or safety constraints)
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
pipe.to(device)

def infer_with_diffusion(chunk: bytes, strength: float = 0.75, guidance: float = 7.5) -> bytes:
    """
    Accepts a binary image chunk, enhances or reconstructs it using diffusion.
    Returns a new image as bytes.
    """
    try:
        image = Image.open(io.BytesIO(chunk)).convert("RGB")
        prompt = "restore damaged image, photorealistic, same scene"
        result = pipe(prompt=prompt, image=image, strength=strength, guidance_scale=guidance).images[0]

        output_buffer = io.BytesIO()
        result.save(output_buffer, format="PNG")
        return output_buffer.getvalue()

    except Exception as e:
        print(f"[DIFFUSION ERROR] {e}")
        return b""
