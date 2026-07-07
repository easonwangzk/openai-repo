from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from a local .env file.
load_dotenv()

# Initialize the API client.
client = OpenAI()
output_path = Path("generated_speech.mp3")

# Stream generated speech directly into a local file.
with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="coral",
    input="This repository helps you learn the OpenAI platform step by step.",
    instructions="Speak in a clear, encouraging, and professional tone.",
) as response:
    response.stream_to_file(output_path)

print(f"Saved speech output to: {output_path.resolve()}")
