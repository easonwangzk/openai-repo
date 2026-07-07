import base64
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from a local .env file.
load_dotenv()

# Initialize the API client.
client = OpenAI()
output_path = Path("generated_study_image.png")

# Generate an image using an image generation tool call.
response = client.responses.create(
    model="gpt-4.1",
    input="Generate a clean desk scene with a laptop, notebook, and coffee mug in soft morning light.",
    tools=[{"type": "image_generation"}],
)

# Extract the first generated image payload from the response.
image_data = [
    item.result
    for item in response.output
    if item.type == "image_generation_call"
]

if not image_data:
    raise RuntimeError("No image data was returned by the API.")

output_path.write_bytes(base64.b64decode(image_data[0]))
print(f"Saved generated image to: {output_path.resolve()}")
