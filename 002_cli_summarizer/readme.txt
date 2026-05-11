### Day 2: The CLI Summarizer

**Focus:** Handling dynamic user input and system instructions.

- **Execution (25 mins):**
    - Create folder `002_cli_summarizer`.
    - Use Python's `input()` function to let the user paste a block of text into the terminal.
    - Separate your prompts: Use a **System Prompt** ("You are a strict summarizer. Output exactly three bullet points.") and a **User Prompt** (the text pasted by the user).
- **Acceptance Criteria:** The script accepts variable length text and returns exactly three formatted bullets.