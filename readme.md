# OpenAI responses API (April 2025)

- basic `client.responses.create()`
- web-search
- reasoning
- function-calling
- file-search

## Requirements

- python 3.12 or above
- dotenv
- OpenAI SDK 1.72.0 or above (OpenAI Python SDK)[https://github.com/openai/openai-python]

## Setup

1. git clone the repo
2. create an environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```
3. install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. create your `.env` file based on `.env.example`
5. run individual scripts `python responses-basic.py` and check the code
