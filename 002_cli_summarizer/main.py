import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Load the environment variables
load_dotenv()

# 2. Initialize the client
client = genai.Client()

# 3. Define the System Instruction (The Constraint)
system_instruction = "You are a strict summarizer. Output exactly three bullet points. Do not include any introductory or concluding text."

print("--- CLI Text Summarizer ---")
print("Paste your messy text below. When finished, type 'DONE' on a new line and press Enter:\n")

# 4. Handle multi-line user input
user_lines = []
while True:
    line = input()
    if line.strip().upper() == 'DONE':
        break
    user_lines.append(line)

user_text = "\n".join(user_lines)

if not user_text.strip():
    print("No text provided. Exiting.")
    sys.exit()

print("\nProcessing...\n")

# 5. Make the API call, passing both the user text and the system config
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=user_text,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.2 # Lower temperature for a highly predictable format
    )
)

# 6. Print the result
print("--- 3-Bullet Summary ---")
print(response.text)