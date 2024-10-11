import requests
from groq import Client

GROQ_API_KEY = "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"


# Initialize the Groq client with your API key
client = Client(api_key=GROQ_API_KEY)


def get_text_explanation(predicted_class):
    """
    Sends a request to the Groq API with a generated prompt for the given predicted class
    and retrieves a detailed medical explanation.

    Args:
        predicted_class (str): The diagnosed medical condition to be explained.

    Returns:
        str: A detailed explanation of the diagnosis, treatment plan, and lifestyle advice.
    """

    # Construct the prompt for the virtual doctor
    prompt = f"""
    You are a virtual doctor. The patient has been diagnosed with {predicted_class}.
    
    1. Diagnose the condition in detail.
    2. Provide a suggested treatment plan.
    3. Offer lifestyle or preventive advice to help manage the condition.
    4. Finally, remind the patient to consult their personal doctor for confirmation and further management.
    """

    try:
        # Send a chat completion request using Groq's client
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",  # Example model, ensure the correct one is used
        )

        # Extract the response text from the chat completion
        explanation = chat_completion.choices[0].message.content

    except requests.RequestException as e:
        print(f"Error contacting Groq API: {e}")
        explanation = "There was an error fetching the explanation. Please try again later."

    return explanation
