Project 006: SOW Reader & Analyzer

The Goal: Build a script that uploads a PDF Statement of Work (SOW) to the Gemini API,
asks for a structured summary and extraction of key project details, and prints the
results—demonstrating file upload, document analysis, and prompt engineering.

What you learn:
- File Upload & Document Handling — Uses client.files.upload() to upload a PDF,
  letting the Gemini backend handle parsing and temporary storage.
- Multi-Modal Prompting — Passes both the uploaded document and a detailed prompt
  to client.models.generate_content(), enabling the model to read and analyze the file.
- Structured Information Extraction — Crafts a prompt that requests a summary,
  deliverables, and timeline, with fallback instructions if data is missing.
- Safety Checks — Verifies the PDF exists before uploading, exiting gracefully if not.
- Output Handling — Prints the AI-generated analysis directly to the console.

How it works (Step by Step):
1. load_dotenv() reads the .env file and loads GEMINI_API_KEY into the environment.
2. genai.Client() initializes the Gemini API client using the loaded API key.
3. Checks if mock_sow.pdf exists in the folder; exits with an error if not found.
4. Uploads the PDF to Gemini's temporary storage using client.files.upload().
5. Defines a prompt instructing the AI to extract a summary, deliverables, and timeline.
6. Calls client.models.generate_content() with both the document and prompt as input.
7. Prints the AI's structured analysis of the SOW to the console.