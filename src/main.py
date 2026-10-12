import gradio as gr
from dotenv import load_dotenv

# 1. Load API keys first
load_dotenv()

# 2. Import the completed modules
from data_processor import read_transcript, clean_text
from llm_processor import create_script
from tts_generator import generate_audio

# 3. Update the wrapper function to accept the voice choice from the UI
def make_recap(file_path, voice_choice):
    if file_path is None:
        raise gr.Error("Please upload a transcript (.txt or .pdf)")
    
    # Process data
    text = clean_text(read_transcript(file_path))
    
    # Generate script
    script = create_script(text)
    
    # Generate audio using the user's selected voice
    audio_path = generate_audio(script, voice=voice_choice)
    
    return script, audio_path

# 4. Build the modern Blocks UI design
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎙️ Podcast Studio: Daily Lesson Recapper")
    gr.Markdown("Upload a class transcript (.txt or .pdf) to instantly generate a 5-minute audio summary.")
    
    with gr.Row():
        # Left Column: Inputs
        with gr.Column():
            file_input = gr.File(label="Upload Document", type="filepath")
            
            # Voice selection dropdown menu
            voice_input = gr.Dropdown(
                choices=["alloy", "echo", "fable", "onyx", "nova", "shimmer"], 
                value="nova", 
                label="Select Podcast Voice"
            )
            
            submit_btn = gr.Button("Generate Podcast", variant="primary")
            
        # Right Column: Outputs
        with gr.Column():
            audio_output = gr.Audio(label="Your Podcast")
            script_output = gr.Textbox(label="Generated Script", lines=10)

    # 5. Connect both inputs (file and voice dropdown) to the master function
    submit_btn.click(
        fn=make_recap,
        inputs=[file_input, voice_input],
        outputs=[script_output, audio_output]
    )

# 6. Launch the server
if __name__ == "__main__":
    demo.launch()