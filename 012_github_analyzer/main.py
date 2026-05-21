import sys
import requests
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Setup Gemini
load_dotenv()
client = genai.Client()

print("--- AI GitHub Repository Analyzer ---")
# Example input format: microsoft/vscode, facebook/react, openai/openai-python
repo_input = input("Enter a public GitHub repo (Format: owner/repo): ")

if "/" not in repo_input:
    print("Invalid format. Please use 'owner/repo'.")
    sys.exit()

print(f"\nFetching data from GitHub API for {repo_input}...\n")

# 2. Call the GitHub REST API (No auth needed for public repos with low volume)
github_api_url = f"https://api.github.com/repos/{repo_input}"
commits_api_url = f"https://api.github.com/repos/{repo_input}/commits?per_page=10"

try:
    # Get general repo info
    repo_response = requests.get(github_api_url)
    repo_response.raise_for_status()
    repo_data = repo_response.json()
    
    # Get recent commits
    commits_response = requests.get(commits_api_url)
    commits_response.raise_for_status()
    commits_data = commits_response.json()

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from GitHub. Make sure the repo exists: {e}")
    sys.exit()

# 3. Format the data for the LLM
repo_description = repo_data.get('description', 'No description provided.')
stars = repo_data.get('stargazers_count', 0)
language = repo_data.get('language', 'Unknown')

# Extract just the commit messages
commit_messages = []
for idx, commit in enumerate(commits_data):
    msg = commit['commit']['message'].split('\n')[0] # Get just the first line
    commit_messages.append(f"{idx+1}. {msg}")

formatted_commits = "\n".join(commit_messages)

ai_payload = f"""
Repository: {repo_input}
Description: {repo_description}
Primary Language: {language}
Stars: {stars}

Recent Commits (Last 10):
{formatted_commits}
"""

# 4. Define the prompt and call Gemini
system_instruction = """
You are a Lead Software Architect. Review the provided GitHub repository metadata and the recent commit history.
Provide a short paragraph summarizing what this project is, and a second paragraph analyzing what the 
engineering team has been actively working on or fixing recently based on the commits.
"""

print("Data retrieved. Sending to AI for architectural analysis...\n")

ai_response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=ai_payload,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.3
    )
)

print("--- 🧠 Architectural Analysis ---")
print(ai_response.text)