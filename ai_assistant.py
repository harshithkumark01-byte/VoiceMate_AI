import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def generate_response(user_message):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Gemini API key not configured.")

    client = genai.Client(api_key=api_key)

    prompt = f"""
    You are VoiceMate AI, a friendly multilingual customer support assistant.

    Answer the customer's question clearly and politely.
    Keep your response concise and easy to understand.

    Customer: {user_message}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text