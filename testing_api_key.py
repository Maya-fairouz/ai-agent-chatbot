import openai

# Paste your key here directly, or load from an .env file
openai.api_key = "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"

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Hello, are you working?"}
        ]
    )
    print("✅ API key is valid. Bot replied:")
    print(response.choices[0].message["content"])

except openai.error.AuthenticationError:
    print("❌ Invalid API key.")

except Exception as e:
    print(f"❌ Something else went wrong: {e}")
