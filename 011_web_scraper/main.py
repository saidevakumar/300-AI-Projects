import sys
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from google import genai

# 1. Setup
load_dotenv()
client = genai.Client()

# 2. Define the target URL (e.g., a tech news article or blog post)
url = input("Enter a URL to analyze: ")

if not url.startswith("http"):
    print("Please enter a valid URL starting with http or https.")
    sys.exit()

print(f"\n--- Scraping {url} ---")

try:
    # 3. Fetch the webpage content
    response = requests.get(url, timeout=10)
    response.raise_for_status() # Check for errors (like a 404 page)
    
    # 4. Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract only the text from paragraphs to avoid sending messy HTML code to the AI
    paragraphs = soup.find_all('p')
    page_text = "\n".join([p.get_text() for p in paragraphs])
    
    if not page_text.strip():
         print("Could not find any readable text on this page.")
         sys.exit()
         
    print("Scrape complete. Sending to AI for summary...\n")
    
except Exception as e:
    print(f"Error fetching the URL: {e}")
    sys.exit()

# 5. Define the instruction
prompt = f"""
You are an executive assistant. Read the following text scraped from a webpage.
Provide a 3-bullet executive summary of the core concepts, and identify 1 potential 
business impact or takeaway for a technology delivery manager.

Text to analyze:
{page_text}
"""

# 6. Make the API call
ai_response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt
)

print("--- Executive Summary ---")
print(ai_response.text)