import re
import PyPDF2

def read_transcript(file_path):
    # Handle PDF files
    if file_path.lower().endswith('.pdf'):
        extracted_text = ""
        with open(file_path, 'rb') as f:  # Note the 'rb' (read binary) mode
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                extracted_text += page.extract_text() + "\n"
        return extracted_text
    
    # Handle standard TXT files
    else:
        with open(file_path, encoding="utf-8") as f:
            return f.read()

def clean_text(text):
    # remove timestamps (12:05), filler words, extra spaces
    text = re.sub(r"\d{1,2}:\d{2}(:\d{2})?", "", text)
    text = re.sub(r"\b(um|uh)\b", "", text, flags=re.I)
    text = re.sub(r"\s+", " ", text)
    return text.strip()