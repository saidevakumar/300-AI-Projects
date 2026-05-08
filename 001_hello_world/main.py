import os
from dotenv import load_dotenv
from google import genai

# 1. Load the environment variables (your API key) from the .env file
load_dotenv()

# 2. Initialize the client. 
# The SDK automatically looks for the GEMINI_API_KEY variable in your environment.
client = genai.Client()

# 3. Define the hardcoded prompt
prompt = "Explain the concept of 'Technical Debt' in one sentence."
print(f"Sending prompt: '{prompt}'\n...\n")

# 4. Make the API call to the model
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
)

# 5. Print the result
print("Response:")
print(response.text)