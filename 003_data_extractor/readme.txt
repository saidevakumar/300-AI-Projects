Project 003: The AI Data Extractor

The Goal: Build a CLI tool that accepts messy, unstructured text (e.g., a project email),
sends it to the Gemini API with strict instructions, and extracts key information into
a clean, validated JSON object with defined fields.

What you learn:
- Structured JSON Output — Uses response_mime_type="application/json" in
  GenerateContentConfig to force the model to return a valid JSON object directly.
- System Instruction as a Schema — Defines specific JSON keys ('sender',
  'priority_level', 'main_request', 'deadline') via the system instruction to
  shape the model's output structure.
- Error Handling & Retry Logic — Catches APIError and specifically handles 429
  (rate limit) errors by waiting 60 seconds and retrying up to 3 times before giving up.
- JSON Validation — Uses json.loads() to parse and validate the response, and
  json.dumps() with indent=4 to pretty-print the result. Falls back to raw output
  if parsing fails.
- Low Temperature for Precision — Sets temperature=0.1 for highly deterministic,
  consistently structured output suited for data extraction tasks.

How it works (Step by Step):
1. load_dotenv() reads the .env file and loads GEMINI_API_KEY into the environment.
2. genai.Client() initializes the Gemini API client using the loaded API key.
3. A system instruction is defined to constrain the model to return only a JSON object
   with four specific keys.
4. The user is prompted to paste messy text line by line, finishing with 'DONE'.
5. All input lines are joined into a single string.
6. client.models.generate_content() sends the text with the system instruction,
   low temperature, and JSON MIME type to the gemini-2.0-flash model.
7. On a 429 rate limit error, the script waits 60 seconds and retries up to 3 times.
8. The response is parsed with json.loads() and pretty-printed with json.dumps().
   If parsing fails, the raw response text is printed instead.