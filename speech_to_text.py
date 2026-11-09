import os
from dotenv import load_dotenv
from gnani.stt import GnaniSTTClient

load_dotenv()

GNANI_API_KEY = os.getenv("GNANI_API_KEY")

if not GNANI_API_KEY:
    raise ValueError("Gnani API key not configured")

# Initialize Gnani Speech-to-Text client
client = GnaniSTTClient(api_key=GNANI_API_KEY)


def transcribe_audio(audio_path, language="en-IN"):

    if not os.path.exists(audio_path):
        raise FileNotFoundError("Audio file not found.")

    try:
        result = client.transcribe(
            audio_path,
            language_code=language
        )

        transcript = result.get("transcript", "")

        if not transcript:
            raise Exception("No speech was recognized.")

        return transcript

    except Exception as e:
        raise Exception(f"Gnani Speech-to-Text Error: {e}")