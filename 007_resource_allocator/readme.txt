Project 007: Resource Allocator

The Goal: Build a script that loads team capacity data from a CSV file, formats it
as a markdown table, and sends it along with a new project request to the Gemini API
to receive AI-powered resource allocation recommendations.

What you learn:
- CSV Data Integration — Uses pandas.read_csv() to load team capacity data and
  convert it to a markdown table with df.to_markdown(), which is the format LLMs
  understand best for structured tabular data.
- Combining Structured Data with Natural Language — Concatenates CSV context and
  a natural language project request into a single prompt string that the AI can reason over.
- System Instruction for Decision Making — Defines a system instruction that sets
  the AI's role as a resource manager, giving it context on how to evaluate and recommend.
- Low Temperature for Logical Output — Sets temperature=0.2 for deterministic,
  logic-driven recommendations rather than creative or unpredictable suggestions.
- Real-World Workflow Simulation — Demonstrates a practical business use case where
  structured data (CSV) and unstructured requests (natural language) are combined
  for intelligent decision support.

How it works (Step by Step):
1. load_dotenv() reads the .env file and loads GEMINI_API_KEY into the environment.
2. genai.Client() initializes the Gemini API client using the loaded API key.
3. pd.read_csv('team_capacity.csv') loads the team capacity data into a DataFrame.
4. df.to_markdown(index=False) converts the DataFrame into a markdown table string,
   which LLMs handle well for tabular reasoning.
5. A system instruction is defined to set the AI's role as a resource manager.
6. A hardcoded new project request is defined describing a React dashboard project.
7. The CSV context and project request are concatenated into a single full_prompt.
8. client.models.generate_content() sends the combined prompt with the system
   instruction and low temperature to the gemini-2.5-flash model.
9. response.text is printed, displaying the AI's resource allocation recommendation.