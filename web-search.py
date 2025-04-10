
from openai import OpenAI
from dotenv import load_dotenv
import os

#SETUP
load_dotenv() # Load environment variables from .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Initialize OpenAI client with API key from environment

# Get location input from user
location = input("Enter the location to check weather for: ")

#Basic web search with responses API
response = client.responses.create(
    model="gpt-4o-mini",
    tools=[{
        "type": "web_search_preview"
    }],
    input=[
        {"role": "developer", "content": "Answer in Czech language."},
        {"role": "user", "content": f"What is the actual weather in {location}?"}]
)

print(response.output_text)
print(response.output[1].content[0].annotations)