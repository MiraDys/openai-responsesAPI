
from openai import OpenAI
from dotenv import load_dotenv
import os

#SETUP
load_dotenv() # Load environment variables from .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Initialize OpenAI client with API key from environment

tools = [
    {
        "type": "function",
        "name": "send_email",
        "description": "Send an email to the user",
        "parameters": {
            "type": "object",
            "properties": {
                "to": {"type": "string", "description": "The email address of the recipient"},
                "subject": {"type": "string", "description": "The subject of the email"},
                "body": {"type": "string", "description": "The body of the email"}
            },
            "required": ["to", "subject", "body"],
            "additionalProperties": False
        }
    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    tools=tools,
    input=[
        {"role": "user", "content": "Send an email to john@snow.com with the subject 'Test1' and the body 'This is a test email.'"}
    ]
)

print(response.output)
print(response.outputp[0].model_dump_json(indent=2))