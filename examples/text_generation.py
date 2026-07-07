from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from a local .env file.
load_dotenv()

# Initialize the OpenAI client with the API key from the environment.
client = OpenAI()

# Use the Responses API for a general-purpose text task.
response = client.responses.create(
    model="gpt-4.1-mini",
    instructions="You are a concise teaching assistant for OpenAI API beginners.",
    input="Explain in five bullet points when to use a smaller model instead of a larger one.",
)

print("Text generation result:\n")
print(response.output_text)
