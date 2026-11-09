import os
from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()

stt = None


def initialize_stt():

    global stt

    if stt is None:

        if not os.getenv("GNANI_API_KEY"):
            raise ValueError("Gnani API key not configured")

        stt = pipeline(
            "automatic-speech-recognition",
            model="gnani/gnani",
            trust_remote_code=True
        )

    return stt


def transcribe_audio(audio_path, language="en-IN"):

    model = initialize_stt()

    result = model(
        audio_path,
        language_code=language
    )

    return result["text"]
