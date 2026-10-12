import gradio as gr
from dotenv import load_dotenv

# Load API keys first
load_dotenv()

# Import the completed modules
from data_processor import read_transcript, clean_text
from llm_processor import create_script
from tts_generator import generate_audio

def make_recap(file_path):
    if file_path is None:
        raise gr.Error("Please upload a transcript (.txt or .pdf)")
    
    # 1. Process data
    text = clean_text(read_transcript(file_path))
    
    # 2. Generate script
    script = create_script(text)
    
    # 3. Generate audio
    audio_path = generate_audio(script)
    
    return script, audio_path

# Build the Gradio UI
demo = gr.Interface(
    fn=make_recap,
    inputs=gr.File(label="Upload a transcript (.txt or .pdf)", type="filepath"),
    outputs=[
        gr.Textbox(label="Recap script"),
        gr.Audio(label="Recap podcast")
    ],
    title="Podcast Reader",
    description="Upload a transcript to generate a short audio summary."
)

if __name__ == "__main__":
    demo.launch()