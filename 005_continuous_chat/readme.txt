Project 005: Stateful AI Chat (Sprint 1 Finale)

The Goal: Build a continuous, stateful CLI chat application that maintains the full
conversation history across turns, allowing the AI to remember and reference previous
messages within the same session.

What you learn:
- Manual State Management — Uses a chat_history list to manually track the full conversation, appending both user and AI messages after every turn.
- Structured Message Format — Wraps each message in types.Content with a role ("user" or "model") and types.Part.from_text() to match the API's expected input format.
- Sending Full Context — Passes the entire chat_history array (not just the latest message) to client.models.generate_content() so the model has full conversational context on every API call.
- Continuous Loop with Exit Condition — Runs an infinite while loop that keeps the chat session alive until the user types 'exit', at which point the session ends and history is cleared.
- Stateless API, Stateful Client — Demonstrates that the Gemini API itself is stateless; memory is achieved purely by resending the growing history on each call.

How it works (Step by Step):
1. load_dotenv() reads the .env file and loads GEMINI_API_KEY into the environment.
2. genai.Client() initializes the Gemini API client using the loaded API key.
3. An empty chat_history list is created to serve as the session memory.
4. A while loop continuously prompts the user for input.
5. If the user types 'exit', the loop breaks and the session ends.
6. The user's message is wrapped in types.Content with role="user" and appended to chat_history.
7. The full chat_history is sent to the gemini-2.5-flash model on every call, giving the AI full context of the conversation so far.
8. The AI's response is printed to the console.
9. The AI's response is wrapped in types.Content with role="model" and appended to chat_history, completing the turn and updating the memory for the next loop.
