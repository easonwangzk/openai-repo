from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from a local .env file.
load_dotenv()

# Initialize the API client.
client = OpenAI()
audio_path = Path("sample_audio.mp3")

if not audio_path.exists():
    raise FileNotFoundError(
        "Place an audio file named sample_audio.mp3 in the examples directory before running this script."
    )

# Send the audio file for transcription.
with audio_path.open("rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        model="gpt-4o-transcribe",
        file=audio_file,
        response_format="text",
    )

print("Transcription result:\n")
print(transcription.text)
