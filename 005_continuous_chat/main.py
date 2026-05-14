import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Setup the environment
load_dotenv()
client = genai.Client()

# 2. Create the empty array for state management (The "Memory")
chat_history = []

print("--- Stateful AI Chat (Sprint 1 Finale) ---")
print("Type 'exit' to end the session.\n")

# 3. The Continuous Loop
while True:
    user_input = input("You: ")
    
    if user_input.strip().lower() == 'exit':
        print("\nSession ended. History cleared.")
        break
        
    # 4. Append the user's new message to the history array
    chat_history.append(
        types.Content(role="user", parts=[types.Part.from_text(text=user_input)])
    )
    
    # 5. Send the ENTIRE history to the API, not just the newest message
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=chat_history
    )
    
    print(f"\nAI: {response.text.strip()}\n")
    
    # 6. Append the AI's response to the history so it remembers for the next loop
    chat_history.append(
        types.Content(role="model", parts=[types.Part.from_text(text=response.text)])
    )