import pandas as pd
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Setup
load_dotenv()
client = genai.Client()

# 2. Load and format the CSV data using Pandas
# Pandas reads the file into a "DataFrame"
df = pd.read_csv('team_capacity.csv')

# We convert the DataFrame into a markdown table string, 
# which is the format LLMs understand best for tabular data.
csv_context = df.to_markdown(index=False) 

print("--- Current Team Capacity ---")
print(csv_context)
print("\n---------------------------\n")

# 3. Define the instruction and the new project request
system_instruction = """
You are an expert technical resource manager. 
Review the provided team capacity table. 
The user will describe a new incoming project. 
Recommend the best team member(s) to assign to the new project based on their 
available hours, skills, and current workload. Justify your recommendation briefly.
"""

new_project_request = "We just landed a rush project to build a new client dashboard interface. It requires heavy React work and we need someone who can dedicate at least 20 hours to it this week."

# 4. Combine the CSV data with the user prompt
full_prompt = f"Team Capacity Data:\n{csv_context}\n\nNew Project Request:\n{new_project_request}"

# 5. Make the API Call
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=full_prompt,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.2, # Low temperature for logical decision making
    )
)

print("--- AI Resource Recommendation ---")
print(response.text)