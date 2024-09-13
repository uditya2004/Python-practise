import os
from gradio_client import Client

client = Client("stabilityai/stable-diffusion-3-medium")
result = client.predict(
    prompt="taj mahal",
    negative_prompt="blurry, low quality, cartoonish, abstract",
    seed=0,
    randomize_seed=True,
    width=1024,
    height=1024,
    guidance_scale=5,
    num_inference_steps=28,
    api_name="/infer"
)

# The result will contain the path to the image.
image_path = result[0]
print(f"Image saved at: {image_path}")

# Automatically open the image using the default image viewer
if os.path.exists(image_path):
    os.startfile(image_path)  # For Windows
else:
    print(f"Image path not found: {image_path}")
