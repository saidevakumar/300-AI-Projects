import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Setup
load_dotenv()
client = genai.Client()

HISTORY_FILE = "chat_history.json"

# 2. Helper function to load memory from disk
def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        raw_data = json.load(f)
    
    # Rebuild the API-specific Content objects
    history = []
    for item in raw_data:
        history.append(
            types.Content(role=item["role"], parts=[types.Part.from_text(text=item["text"])])
        )
    return history

# 3. Helper function to save memory to disk
def save_history(history):
    raw_data = []
    for item in history:
        raw_data.append({"role": item.role, "text": item.parts[0].text})
    
    with open(HISTORY_FILE, "w") as f:
        json.dump(raw_data, f, indent=4)

# 4. Initialize by loading the past memory
chat_history = load_history()

print("--- The Persistent AI Assistant ---")
print("I remember our previous sessions. Type 'exit' to quit or 'clear' to wipe memory.\n")

# 5. The Chat Loop
while True:
    user_input = input("You: ")
    
    if user_input.strip().lower() == 'exit':
        print("Session ended. Memory saved to disk.")
        break
        
    if user_input.strip().lower() == 'clear':
        chat_history = []
        save_history(chat_history)
        print("Memory wiped!")
        continue

    # Append user message and call API
    chat_history.append(types.Content(role="user", parts=[types.Part.from_text(text=user_input)]))
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=chat_history
    )
    
    print(f"\nAI: {response.text.strip()}\n")
    
    # Append model response and immediately save to disk
    chat_history.append(types.Content(role="model", parts=[types.Part.from_text(text=response.text)]))
    save_history(chat_history)