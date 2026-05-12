Project 002: The CLI Text Summarizer

The Goal: Build a command-line tool that accepts multi-line text input from the user,
sends it to the Gemini API with a strict system instruction, and prints a clean
3-bullet-point summary of the provided text.

What you learn:
- System Instructions — Uses types.GenerateContentConfig to pass a system_instruction
  that constrains the model to output exactly three bullet points with no extra text.
- Multi-line CLI Input — Captures multiple lines of user input in a loop, stopping
  when the user types 'DONE' on a new line.
- Temperature Control — Sets temperature=0.2 to make the model's output highly
  predictable and consistently formatted.
- Input Validation — Checks if the user provided any text before making the API call,
  exiting gracefully if no input is given.

How it works (Step by Step):
1. load_dotenv() reads the .env file and loads GEMINI_API_KEY into the environment.
2. genai.Client() initializes the Gemini API client using the loaded API key.
3. A system instruction is defined to strictly constrain the model's response format.
4. The user is prompted to paste text line by line, finishing with 'DONE'.
5. All input lines are joined into a single string and validated.
6. client.models.generate_content() sends the user text along with the system
   instruction and temperature config to the gemini-2.5-flash model.
7. response.text extracts and prints the 3-bullet summary from the response object.