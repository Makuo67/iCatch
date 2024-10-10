import requests

GROQ_API_KEY = "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"


def get_text_explanation(predicted_class):
    # Construct a virtual doctor prompt
    prompt = f"""
    You are a virtual doctor. The patient has been diagnosed with {predicted_class}.
    
    1. Diagnose the condition in detail.
    2. Provide a suggested treatment plan.
    3. Offer lifestyle or preventive advice to help manage the condition.
    4. Finally, remind the patient to consult their personal doctor for confirmation and further management.
    """

    # Prepare API request to Groq
    payload = {
        "model": "llama-3.1-8b-instant",  # Example of a selected model
        "messages": [{"role": "user", "content": prompt}],
    }
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        # Send request to Groq API
        response = requests.post(
            "https://api.groq.ai/explain", json=payload, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        explanation = response.json().get("choices", [{}])[0].get(
            "message", {}).get("content", "No explanation available.")
    except requests.RequestException as e:
        print(f"Error contacting Groq API: {e}")
        explanation = "There was an error fetching the explanation. Please try again later."

    return explanation
