from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key from environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def response_with_topic(topic):
    items = [{"role": "user", "content": f"tell me a joke about the topic the user has provided: {topic}"}]
    response = client.responses.create(
        model="gpt-4o-mini",
        input=items,
        instructions="You are a helpful assistant that tells jokes.",
        
    )
    print(response.output_text)
    return response

def simple_response():
    response = client.responses.create(
        model="gpt-4o",
        input="Write a two sentence paragraph about data science",
    )
    print(response.output_text)
    return response

def response_stream_to_terminal():
    stream = client.responses.create(
        model="gpt-4o-mini",
        input="Write a four sentence paragraph about data science",
        stream=True
    )
    text_chunks = []
    for event in stream:
        if hasattr(event, "type") and "text.delta" in event.type:
            text_chunks.append(event.delta)
            print(event.delta, end="", flush=True)

def show_menu():
    print("\nAvailable functions:")
    print("1. Simple response")
    print("2. Response expanded with instructions")
    print("3. Stream a response about data science")
    print("4. Exit")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-4): "))
            if choice == 1:
                simple_response()
            elif choice == 2:
                topic = input("Enter a topic for the joke: ")
                response_with_topic(topic)
            elif choice == 3:
                response_stream_to_terminal()
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

show_menu()
