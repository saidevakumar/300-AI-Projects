import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Setup the environment
load_dotenv()
client = genai.Client()

# 2. Define the Persona Constraint
system_instruction = """
You are an expert executive communication assistant. 
Rewrite the user's message into a highly polished, objective, and solution-oriented 
update suitable for senior leadership. Remove all emotion, blame, and informality. 
Keep it concise and focus on the business impact and next steps.
"""

# 3. The raw, blunt input (The problem we are trying to solve)
raw_message = """
The client keeps changing the scope every two seconds and it's driving the dev team crazy. 
If they don't lock down the requirements today, we are going to miss the deadline and it's entirely their fault.
"""

print("--- RAW INPUT ---")
print(raw_message.strip() + "\n")

# 4. The API Call with Parameter Tuning
response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents=raw_message,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.01, # Low temperature = highly predictable, non-creative, objective text
    )
)

# 5. Print the result
print("--- POLISHED OUTPUT ---")
print(response.text.strip())