import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("Gemini API key not found in .env file")

client = genai.Client(
    api_key=GEMINI_API_KEY
)


def generate_response(user_input):

    if not user_input or not user_input.strip():
        raise ValueError("Please enter a valid question.")

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=user_input,
            config=types.GenerateContentConfig(
                max_output_tokens=300,
                temperature=0.7
            )
        )

        if not response.text:
            raise Exception("Gemini returned an empty response.")

        return response.text

    except Exception as e:
        raise Exception(f"Gemini API Error: {e}")