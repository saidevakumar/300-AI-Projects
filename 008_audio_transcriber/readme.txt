Project 008: Audio Transcriber & Stand-up Analyzer

The Goal: Build a script that uploads an audio file (MP3) of a daily stand-up meeting
to the Gemini API and extracts structured information — team member name, yesterday's
work, today's plan, and blockers — directly from the spoken audio content.

What you learn:
- Audio File Upload — Uses client.files.upload() to upload an MP3 file to Gemini's temporary storage, letting the backend handle audio processing automatically.
- Multi-Modal Prompting with Audio — Passes both the uploaded audio file object and a structured text prompt to client.models.generate_content(), enabling the model
  to listen and extract information from spoken content.
- Structured Extraction via Prompt Engineering — Crafts a prompt that defines an exact output format (team member, yesterday, today, blockers) rather than just
  requesting a raw transcription.
- Safety Check — Verifies the audio file exists before attempting upload, exiting gracefully with an error message if not found.
- Optional Cleanup — Includes a commented-out client.files.delete() call to remove the uploaded file from Gemini's temporary storage after processing.

How it works (Step by Step):
1. load_dotenv() reads the .env file and loads GEMINI_API_KEY into the environment.
2. genai.Client() initializes the Gemini API client using the loaded API key.
3. Checks if standup.mp3 exists in the folder; exits with an error if not found.
4. Uploads the MP3 file to Gemini's temporary storage using client.files.upload().
5. Defines a structured prompt instructing the AI to extract stand-up details in a specific format with four defined fields.
6. client.models.generate_content() sends both the audio file object and the text prompt to the gemini-2.5-flash model for multi-modal processing.
7. response.text is printed, displaying the structured stand-up analysis extracted directly from the audio content.