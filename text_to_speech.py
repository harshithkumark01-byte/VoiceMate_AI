import os
from dotenv import load_dotenv
from gnani.tts import GnaniTTSClient, AudioConfig

load_dotenv(
    dotenv_path=os.path.join(
        os.path.dirname(__file__),
        ".env"
    )
)

def generate_speech(text, language="en-IN"):

    api_key = os.getenv("GNANI_API_KEY")

    if not api_key:
        raise ValueError(
            "Gnani API key not found. Check your .env file."
        )

    client = GnaniTTSClient(api_key=api_key)

    audio = client.synthesize(
        text,
        voice="Nalini",
        model="timbre-v2.5",
        language=language,
        audio_config=AudioConfig(
            sample_rate=48000,
            encoding="linear_pcm",
            container="wav"
        )
    )

    return audio