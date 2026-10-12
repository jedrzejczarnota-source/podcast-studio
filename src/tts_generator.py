from pathlib import Path
from openai import OpenAI

# Load the API key from the .env file
BASE_DIR = Path(__file__).resolve().parent.parent

# Connect to OpenAI
client = OpenAI()


def generate_audio(script, voice="alloy", path="outputs/recap.mp3"):
    # Create the output folder if it doesn't exist
    output_path = BASE_DIR / path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Convert the podcast script into speech
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,  # This now uses the variable passed from main.py
        input=script,
    )
    
    # Save the audio as an MP3 file
    response.write_to_file(output_path)
    return path

    # Return the location of the generated audio
    return str(output_path)