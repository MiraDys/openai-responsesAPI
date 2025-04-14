
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def reasoning(prompt):
    response = client.responses.create(
    model="o3-mini",
    reasoning={"effort": "medium"},
    input=[{
        "role": "user",
        "content": prompt
    }]
)
    print(response.output_text)

reasoning("Write a 250 word essay about data science being irreplaceable in the future.")
