Project 010: Persistent AI Chat Log

The Goal: Build a chat assistant that remembers the full conversation history across sessions by saving and loading chat logs to disk, enabling persistent memory between runs.

What you learn:
- Persistent State Management — Implements helper functions to load and save chat history as JSON, allowing the assistant to remember previous conversations even after restarting the script.
- Structured Message Handling — Converts between API-specific Content objects and plain JSON for serialization and deserialization.
- Continuous Chat Loop — Maintains a chat loop where user and AI messages are appended to history and saved after every turn.
- Special Commands — Supports 'exit' to quit and save memory, and 'clear' to wipe the chat history from both memory and disk.
- Full Context on Every Call — Sends the entire chat history to the Gemini API on each request, ensuring the AI has access to all prior context.
- File I/O for Memory — Demonstrates reading from and writing to a local JSON file (chat_history.json) for persistent storage.

How it works (Step by Step):
1. load_dotenv() loads GEMINI_API_KEY from the environment.
2. genai.Client() initializes the Gemini API client.
3. load_history() loads previous chat history from chat_history.json and rebuilds Content objects.
4. The chat loop prompts the user for input.
5. If 'exit' is typed, the session ends and memory is saved.
6. If 'clear' is typed, the chat history is wiped from memory and disk.
7. User messages are appended to chat_history and sent to the Gemini API.
8. AI responses are appended to chat_history and the updated history is saved to disk after each turn.