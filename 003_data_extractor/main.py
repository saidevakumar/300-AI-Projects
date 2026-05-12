import json
from dotenv import load_dotenv
from google import genai
from google.genai import types
import time
from google.genai.errors import APIError

# 1. Setup
load_dotenv()
client = genai.Client()

# 2. The Instruction - Explicitly asking for JSON
system_instruction = """
You are a data extraction bot. Your goal is to extract key information from messy text. 
You must return ONLY a valid JSON object. Do not include markdown formatting or backticks.
The JSON must have these keys: 'sender', 'priority_level', 'main_request', and 'deadline'.
"""

print("--- AI Data Extractor ---")
print("Paste a messy project email or update (Type 'DONE' to process):\n")

user_lines = []
while True:
    line = input()
    if line.strip().upper() == 'DONE':
        break
    user_lines.append(line)

user_text = "\n".join(user_lines)

# 3. Execution
max_retries = 3
retry_delay = 60 # wait 60 seconds if we hit a quota limit

for attempt in range(max_retries):
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=user_text,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.1, 
                response_mime_type="application/json" 
            )
        )
        # If successful, parse the JSON and break the loop
        import json
        data = json.loads(response.text)
        print("\n--- Validated JSON Output ---")
        print(json.dumps(data, indent=4))
        break 
        
    except APIError as e:
        if e.code == 429:
            print(f"Rate limit hit. Waiting {retry_delay} seconds before retry {attempt + 1}/{max_retries}...")
            time.sleep(retry_delay)
        else:
            # If it's a different error, print it and stop
            print(f"An unexpected API error occurred: {e}")
            break

# 4. Parsing the result to prove it's valid JSON
try:
    data = json.loads(response.text)
    print("\n--- Validated JSON Output ---")
    print(json.dumps(data, indent=4))
except json.JSONDecodeError:
    print("\n--- Raw Output (Parsing Failed) ---")
    print(response.text)