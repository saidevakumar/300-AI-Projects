import os
import sys
import time
from dotenv import load_dotenv
from google import genai

# 1. Setup
load_dotenv()
client = genai.Client()

file_name = 'standup.mp3'

if not os.path.exists(file_name):
    print(f"Error: Could not find {file_name}. Please add an audio file to the folder.")
    sys.exit()

print(f"--- Uploading {file_name} to Gemini ---")

# 2. Upload the audio file to Google
audio_file = client.files.upload(file=file_name)

print("Upload complete. Processing audio...\n")

# 3. Define the extraction prompt
# We aren't just transcribing; we are structuring the update.
prompt = """
Listen to the attached daily stand-up update.
Extract the information into the following structured format:

1. Team Member: [Name]
2. What was done yesterday: [Brief summary]
3. What is planned for today: [Brief summary]
4. Blockers/Risks: [List any blockers or write 'None']
"""

# 4. Make the API call, passing BOTH the audio file object and the text prompt
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[audio_file, prompt]
)

print("--- Stand-up Analysis ---")
print(response.text)

# Optional cleanup: Delete the file from Google's temporary storage when done
# client.files.delete(name=audio_file.name)