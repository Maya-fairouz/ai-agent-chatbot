# import openai
# from config import OPENAI_API_KEY

# class Agent:
#     def __init__(self):
#         openai.api_key = OPENAI_API_KEY
#         openai.base_url = "https://api.openai.com/v1"  # Default OpenAI endpoint
#         print(f"Using base URL: {openai.base_url}")  # Debug endpoint

#     def get_response(self, message):
#         try:
#             response = openai.chat.completions.create(
#                 model="gpt-3.5-turbo",  # Adjust if your provider uses a different model
#                 messages=[{"role": "user", "content": message}]
#             )
#             print(f"Raw response: {response}")  # Debug raw response
#             if isinstance(response, str):
#                 return response
#             elif hasattr(response, 'choices'):
#                 return response.choices[0].message.content
#             else:
#                 raise ValueError("Unexpected response format")
#         except openai.NotFoundError as e:
#             print(f"Endpoint error: {e}")
#             raise
#         except openai.AuthenticationError as e:
#             print(f"Auth error: {e}")
#             raise
#         except Exception as e:
#             print(f"Unexpected error: {e}")
#             raise


import random
#from config import OPENAI_API_KEY


class Agent:
    def __init__(self):
        self.responses = [
            "Hello! How can I assist you today?",
            "I'm just a simulation, but I think you're great!",
            "Let me think... How about a joke? Why did the computer go to therapy? It had too many bytes of emotional baggage!",
            "Sorry, I’m simulated and don’t have all the answers yet.",
            "boy shut the fuck up",
            "fuck off",
            "That’s an interesting question! Let’s pretend the answer is 42."
        ]

    def get_response(self, message):
        # Simple simulation logic based on input
        if "hello" in message.lower():

            return "Hi there! Nice to meet you!"
        elif "joke" in message.lower():
            return "Why don’t skeletons fight each other? Because they don’t have the guts! 😂"
        elif "time" in message.lower():
            return f"The current time is 12:18 AM CET, July 0Z, 2023."
        else:
            # Random response for other inputs
            return random.choice(self.responses)