import os
import sys
from dotenv import load_dotenv
from google import genai

# 1. Setup
load_dotenv()
client = genai.Client()

file_name = 'mock_sow.pdf'

# Safety check
if not os.path.exists(file_name):
    print(f"Error: Could not find {file_name}. Please add a PDF to the folder.")
    sys.exit()

print(f"--- Uploading {file_name} to Gemini ---")

# 2. Upload the file to Google's temporary storage
# This handles the complex PDF parsing automatically on the backend
document = client.files.upload(file=file_name)

print("Upload complete. Analyzing document...\n")

# 3. Define the extraction prompt
prompt = """
You are a senior technical project manager reviewing a new Statement of Work.
Read the attached document and extract the following:
1. A 2-sentence summary of the overall project goal.
2. The primary deliverables.
3. The estimated timeline or deadlines mentioned.
If any of this information is missing from the document, state 'Not explicitly defined'.
"""

# 4. Make the API call, passing BOTH the document and the prompt
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[document, prompt]
)

# 5. Print the analysis
print("--- Document Analysis ---")
print(response.text)