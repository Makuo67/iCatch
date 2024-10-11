from groq import Client

# Initialize the Groq client with your API key
client = Client(
    api_key='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')

# Example of making a request (this may vary depending on your specific use case)
# Replace 'some_method' and 'params' with actual method and parameters


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)
