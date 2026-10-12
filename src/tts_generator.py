from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Load the API key from the .env file
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# Connect to OpenAI
client = OpenAI()


def generate_audio(script, path="outputs/recap.mp3"):
    # Create the output folder if it doesn't exist
    output_path = BASE_DIR / path
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Convert the podcast script into speech
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=script,
    )

    # Save the audio as an MP3 file
    response.write_to_file(output_path)

    # Return the location of the generated audio
    return str(output_path)