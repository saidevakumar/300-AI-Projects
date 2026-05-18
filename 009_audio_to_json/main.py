import os
import sys
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Setup
load_dotenv()
client = genai.Client()

file_name = 'standup.mp3'

if not os.path.exists(file_name):
    print(f"Error: Could not find {file_name}. Please add an audio file.")
    sys.exit()

print(f"--- Processing Audio: {file_name} ---")

# 2. Upload the audio file
audio_file = client.files.upload(file=file_name)
print("Upload complete. Generating Jira ticket data...\n")

# 3. Define the System Instruction for JSON extraction
system_instruction = """
You are an expert technical project manager. Listen to the provided audio file.
Extract the action items or blockers mentioned and format them as a JSON object 
representing a Jira ticket.

You must return ONLY valid JSON with the following structure:
{
  "summary": "A short, descriptive title for the ticket",
  "assignee": "The name of the person who needs to act",
  "description": "A detailed explanation of the task or blocker",
  "priority": "High, Medium, or Low based on the context",
  "issue_type": "Task or Bug"
}
"""

# 4. Make the API call, forcing JSON output while analyzing audio
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[audio_file, "Generate the JSON Jira ticket based on the audio."],
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.1, # Keep it deterministic for data extraction
        response_mime_type="application/json" # Force machine-readable output
    )
)

# 5. Parse and Print the Result
try:
    ticket_data = json.loads(response.text)
    print("--- 🎫 Generated Jira Ticket (JSON) ---")
    print(json.dumps(ticket_data, indent=4))
except json.JSONDecodeError:
    print("\n--- Error: Could not parse JSON ---")
    print(response.text)

# Cleanup
client.files.delete(name=audio_file.name)