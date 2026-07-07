from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from a local .env file.
load_dotenv()

# Initialize the API client.
client = OpenAI()

# Replace this URL with your own public image URL when testing.
image_url = "https://images.unsplash.com/photo-1515879218367-8466d910aaa4"

# Ask the model to analyze the image content.
response = client.responses.create(
    model="gpt-4.1-mini",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Describe the image and list three details that might matter in a product demo.",
                },
                {
                    "type": "input_image",
                    "image_url": image_url,
                },
            ],
        }
    ],
)

print("Vision analysis result:\n")
print(response.output_text)
