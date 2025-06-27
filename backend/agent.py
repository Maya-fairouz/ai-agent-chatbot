import openai
from config import OPENAI_API_KEY

class Agent:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        openai.base_url = "https://api.openai.com/v1"  # Default OpenAI endpoint
        print(f"Using base URL: {openai.base_url}")  # Debug endpoint

    def get_response(self, message):
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",  # Adjust if your provider uses a different model
                messages=[{"role": "user", "content": message}]
            )
            print(f"Raw response: {response}")  # Debug raw response
            if isinstance(response, str):
                return response
            elif hasattr(response, 'choices'):
                return response.choices[0].message.content
            else:
                raise ValueError("Unexpected response format")
        except openai.NotFoundError as e:
            print(f"Endpoint error: {e}")
            raise
        except openai.AuthenticationError as e:
            print(f"Auth error: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise