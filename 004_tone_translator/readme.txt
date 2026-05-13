Project 004: The Tone Translator

The Goal: Build a script that takes a raw, emotionally charged or informal message
and rewrites it into a polished, professional executive-level communication using
a persona-driven system instruction and precise temperature tuning.

What you learn:
- Persona-Driven System Instructions — Defines a specific AI persona (executive
  communication assistant) via system_instruction to control the style, tone, and
  structure of the model's output.
- Hardcoded Prompt as a Real-World Problem — Uses a realistic, blunt raw message
  as the input to simulate a common workplace communication challenge.
- Ultra-Low Temperature for Objectivity — Sets temperature=0.01 to produce highly
  deterministic, non-creative, and consistently professional output with minimal
  variation between runs.
- Prompt Engineering for Tone Control — Instructs the model to strip emotion, blame,
  and informality while focusing on business impact and next steps.

How it works (Step by Step):
1. load_dotenv() reads the .env file and loads GEMINI_API_KEY into the environment.
2. genai.Client() initializes the Gemini API client using the loaded API key.
3. A system instruction is defined to set the AI's persona as an executive
   communication assistant with strict tone and formatting rules.
4. A hardcoded raw message is defined simulating an emotional, blame-filled
   project status update.
5. The raw message is printed to the console as the "before" output.
6. client.models.generate_content() sends the raw message with the system instruction
   and temperature=0.01 to the gemini-2.5-flash model.
7. response.text is stripped and printed as the polished "after" output, demonstrating
   the tone transformation.