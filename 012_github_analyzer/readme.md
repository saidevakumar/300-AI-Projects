Project 012: AI GitHub Repository Analyzer

The Goal: Build a script that fetches metadata and recent commit history from a public GitHub repository, then sends this information to the Gemini API for an architectural summary and analysis of recent engineering activity.

What you learn:
- GitHub API Integration — Uses requests to call the GitHub REST API for repository metadata and the last 10 commit messages, handling errors and formatting responses.
- Data Formatting for LLMs — Extracts and formats repository details (description, language, stars) and commit messages into a structured payload for the AI.
- Prompt Engineering for Technical Analysis — Crafts a system instruction that asks the AI to summarize the project and analyze recent engineering work based on commit history.
- Combining External Data with AI — Demonstrates how to automate data collection from third-party APIs and use AI for high-level technical insight.
- API Integration — Sends the formatted data and instructions to the Gemini API and prints the AI-generated architectural analysis.

How it works (Step by Step):
1. load_dotenv() loads GEMINI_API_KEY from the environment.
2. genai.Client() initializes the Gemini API client.
3. Prompts the user for a GitHub repository in owner/repo format and validates input.
4. Uses requests to fetch repository metadata and the last 10 commits from the GitHub API.
5. Extracts and formats the repo description, language, stars, and commit messages.
6. Defines a system instruction for the AI to provide a summary and analysis.
7. Calls client.models.generate_content() with the formatted data and system instruction.
8. Prints the AI's architectural analysis of the repository and its recent activity.