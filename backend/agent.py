import openai
from config import OPENAI_API_KEY

class Agent:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        openai.base_url = "https://api.x.ai/v1"  # Replace with actual endpoint from docs

    def get_response(self, message):
        response = openai.chat.completions.create(
            model="grok-3",  # Confirm model name from docs
            messages=[{"role": "user", "content": message}]
        )
        if isinstance(response, str):
            return response
        return response.choices[0].message.content