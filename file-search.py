import requests
from io import BytesIO
from openai import OpenAI
import textwrap
from dotenv import load_dotenv
import os

#SETUP
load_dotenv() # Load environment variables from .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Initialize OpenAI client with API key from environment

def create_file(client, file_path):
    # If the file is a URL, download it and upload it to OpenAI
    if file_path.startswith("https://") or file_path.startswith("http://"):
        response = requests.get(file_path)
        file_content = BytesIO(response.content)
        file_name = file_path.split("/")[-1]
        file_tuple = (file_name, file_content)
        result = client.files.create(file=file_tuple, purpose="assistants")
        return result
    else:
        # If the file is a local file, upload it to OpenAI
        with open(file_path, "rb") as file_content:
            result = client.files.create(file=file_content, purpose="assistants")
            return result
    print(result.id)
    return result.id



