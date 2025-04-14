import requests
from io import BytesIO
from openai import OpenAI
import textwrap
from dotenv import load_dotenv
import os
from time import sleep

#SETUP
load_dotenv() # Load environment variables from .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY_RAG")) # Initialize OpenAI client with API key from environment

def create_file(client, file_path):
    # If the file is a URL, download it and upload it to OpenAI
    # works with PDFs and file type-likes such as .docx, .txt, etc.
    if file_path.startswith("https://") or file_path.startswith("http://"):
        response = requests.get(file_path)
        file_content = BytesIO(response.content)
        file_name = file_path.split("/")[-1]
        file_tuple = (file_name, file_content)
        result = client.files.create(file=file_tuple, purpose="assistants")
        print(result.id)
        return result
    else:
        # If the file is a local file, upload it to OpenAI
        with open(file_path, "rb") as file_content:
            result = client.files.create(file=file_content, purpose="assistants")
            print(result.id)
            return result


file_id = create_file(client, "https://www.cloudflare.com/resources/assets/slt3lc6tev37/3HWObubm6fybC0FWUdFYAJ/5d5e3b0a4d9c5a7619984ed6076f01fe/Cloudflare_for_Campaigns_Security_Guide.pdf")


vector_store_file = client.vector_stores.files.create(
  vector_store_id=os.getenv("VECTOR_STORE_ID"),
  file_id=file_id.id
)
print(vector_store_file.id)


sleep(60)

def search_file(client):
    response = client.responses.create(
        model="gpt-4o-mini",
        tools=[{
      "type": "file_search",
      "vector_store_ids": [os.getenv("VECTOR_STORE_ID")],
      "max_num_results": 4
    }],
    input="What does the document say about authoritative DNS?",
)
    print(response)
    print(textwrap.fill(response.output_text, width=80))

search_file(client)
