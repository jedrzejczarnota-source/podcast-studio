from openai import OpenAI
client = OpenAI()

SYSTEM_PROMPT = (
    "You are a friendly teaching assistant. "
    "Extract the 5 most important learning "
    "points and write a 5-minute recap script."
)

def create_script(transcript):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": transcript},
    ]
    response = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=messages
    )
    return response.choices[0].message.content
