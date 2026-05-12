Project 001: The "Hello World" API Call

The Goal: Prove the plumbing works. Write a script that sends a hardcoded string ("Explain the concept of 'Technical Debt' in one sentence.") to the Gemini API and prints the response.

What you learn:
- Authentication — Uses dotenv to load GEMINI_API_KEY from a .env file securely, keeping secrets out of source code.
- Basic API client initialization — Instantiates the genai.Client() which automatically picks up the API key from the environment.
- Parsing a response object — Calls client.models.generate_content() with the gemini-2.5-flash model and extracts the result via response.text.