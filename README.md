# 🎙️ Podcast Studio: Daily Lesson Recapper

Podcast Studio is a Python-based Gradio web application built to convert raw class transcripts into a 5-minute audio podcast summary. 

It takes a `.txt` or `.pdf` file, extracts and cleans the text, generates a condensed learning script using OpenAI's LLM, and converts that script into speech using OpenAI's TTS API.

## 📦 Project Structure

The pipeline is modularized into dedicated Python files:
* `src/data_processor.py`: Handles file uploading and text cleaning (strips timestamps and filler words).
* `src/llm_processor.py`: Communicates with OpenAI to extract the top 5 key learning points and write the podcast script.
* `src/tts_generator.py`: Converts the written script into an `.mp3` audio file.
* `src/main.py`: The Gradio front-end interface that connects the modules.

## ⚙️ Setup and Installation

**1. Clone the repository**
```bash
git clone [https://github.com/jedrzejczarnota-source/podcast-studio.git]
cd podcast-studio