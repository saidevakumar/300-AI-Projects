Project 009: Audio to JSON Jira Ticket Generator

The Goal: Build a script that uploads an audio file (e.g., a stand-up update) to the Gemini API, analyzes the spoken content, and extracts action items or blockers as a structured JSON object formatted for Jira ticket creation.

What you learn:
- Audio File Upload — Uses client.files.upload() to send an MP3 file to Gemini's temporary storage for backend audio processing.
- System Instruction for Structured Output — Crafts a detailed system_instruction to force the model to return only valid JSON with specific fields for Jira tickets (summary, assignee, description, priority, issue_type).
- Forcing JSON Output — Sets response_mime_type="application/json" in GenerateContentConfig to ensure the model's response is machine-readable JSON.
- Deterministic Extraction — Uses a low temperature (0.1) for consistent, reliable data extraction from audio.
- JSON Parsing and Error Handling — Attempts to parse the model's response with json.loads(); if parsing fails, prints the raw output for debugging.
- Resource Cleanup — Deletes the uploaded audio file from Gemini's temporary storage after processing.

How it works (Step by Step):
1. load_dotenv() loads GEMINI_API_KEY from the environment.
2. genai.Client() initializes the Gemini API client.
3. Checks if standup.mp3 exists; exits with an error if not found.
4. Uploads the audio file to Gemini using client.files.upload().
5. Defines a system instruction to extract Jira ticket fields from the audio.
6. Calls client.models.generate_content() with the audio file, a prompt, and config enforcing JSON output.
7. Attempts to parse the response as JSON and pretty-prints it; if parsing fails, prints the raw response.
8. Deletes the uploaded audio file from Gemini's storage to clean up resources.