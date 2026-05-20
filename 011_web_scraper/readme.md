Project 011: Web Scraper & Executive Summarizer

The Goal: Build a script that scrapes the main text content from a user-provided URL, sends it to the Gemini API, and returns a concise executive summary with a business takeaway.

What you learn:
- Web Scraping Basics — Uses requests to fetch webpage content and BeautifulSoup to parse HTML and extract readable text from paragraph tags.
- Input Validation — Checks that the provided URL starts with http/https and that the page contains readable text before proceeding.
- Error Handling — Handles HTTP errors and missing content gracefully, exiting with informative messages.
- Prompt Engineering for Summarization — Crafts a prompt that instructs the AI to provide a 3-bullet executive summary and a business impact/takeaway for a technology delivery manager.
- Combining Automation with AI — Demonstrates how to automate data collection (web scraping) and then use AI for high-level analysis and summarization.
- API Integration — Sends the scraped text to the Gemini API and prints the AI-generated summary.

How it works (Step by Step):
1. load_dotenv() loads GEMINI_API_KEY from the environment.
2. genai.Client() initializes the Gemini API client.
3. Prompts the user for a URL and validates its format.
4. Uses requests to fetch the webpage and BeautifulSoup to extract paragraph text.
5. Checks for readable text; exits if none is found.
6. Defines a prompt for the AI to summarize the scraped content and identify a business takeaway.
7. Calls client.models.generate_content() with the prompt and prints the AI's executive summary.