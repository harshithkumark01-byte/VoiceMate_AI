import streamlit as st
import os
import tempfile
from dotenv import load_dotenv

from speech_to_text import transcribe_audio
from text_to_speech import generate_speech
from ai_assistant import generate_response

# Load API keys
load_dotenv()

GNANI_API_KEY = os.getenv("GNANI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Page configuration
st.set_page_config(
    page_title="VoiceMate AI",
    page_icon="🎙️",
    layout="wide"
)

# Session state
if "transcript" not in st.session_state:
    st.session_state.transcript = ""

if "ai_reply" not in st.session_state:
    st.session_state.ai_reply = ""

# Language codes
language_codes = {
    "English": "en-IN",
    "Kannada": "kn-IN",
    "Hindi": "hi-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN"
}

# Application heading
st.title("🎙️ VoiceMate AI")
st.subheader("Multilingual AI Customer Support Assistant")

st.write(
    "Speak naturally and get intelligent AI-powered "
    "customer support in your preferred language."
)

# API status
col1, col2 = st.columns(2)

with col1:
    if GNANI_API_KEY:
        st.success("Gnani AI connected")
    else:
        st.error("Gnani API key not configured")

with col2:
    if GEMINI_API_KEY:
        st.success("Gemini AI connected")
    else:
        st.error("Gemini API key not configured")

st.divider()

# Language selection
language = st.selectbox(
    "🌐 Choose your language",
    ["English", "Kannada", "Hindi", "Tamil", "Telugu"]
)

st.write("Selected language:", language)

# Speech input
st.header("🎤 Speak to VoiceMate AI")

audio = st.audio_input("Record your voice")

if audio:
    st.audio(audio)

    if st.button("🚀 Process My Voice", type="primary"):

        audio_path = None

        try:
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".wav"
            ) as temp_audio:

                temp_audio.write(audio.getvalue())
                audio_path = temp_audio.name

            # Speech to text
            with st.spinner("Converting your speech into text..."):

                transcript = transcribe_audio(
                    audio_path,
                    language_codes[language]
                )

            st.session_state.transcript = transcript

            # Gemini AI response
            with st.spinner("Gemini is generating your answer..."):

                ai_reply = generate_response(transcript)

            st.session_state.ai_reply = ai_reply

            st.success("Your request has been processed!")

        except Exception as e:
            st.error(f"Processing failed: {e}")

        finally:
            if audio_path and os.path.exists(audio_path):
                os.remove(audio_path)

# Display conversation
if st.session_state.transcript:

    st.divider()

    st.header("📝 Recognized Speech")

    st.write(st.session_state.transcript)

    st.header("🤖 VoiceMate AI Response")

    st.write(st.session_state.ai_reply)

    # Convert AI response into voice
    if st.button("🔊 Speak AI Response"):

        try:
            with st.spinner("Generating AI voice..."):

                audio_output = generate_speech(
                    st.session_state.ai_reply,
                    language=language_codes[language]
                )

            st.success("AI voice generated successfully!")

            st.audio(audio_output, format="audio/wav")

        except Exception as e:
            st.error(f"Voice generation failed: {e}")

# Manual text to speech
st.divider()

st.header("🔊 Text to Speech")

response_text = st.text_area(
    "Enter text to convert into speech:",
    "Hello! Welcome to VoiceMate AI. How can I help you today?"
)

if st.button("Generate Voice"):

    if response_text.strip():

        try:
            with st.spinner("Generating AI voice..."):

                audio_output = generate_speech(
                    response_text,
                    language=language_codes[language]
                )

            st.success("Voice generated successfully!")

            st.audio(audio_output, format="audio/wav")

        except Exception as e:
            st.error(f"Voice generation failed: {e}")

    else:
        st.warning("Please enter some text.")

st.divider()

st.caption("VoiceMate AI | Powered by Gnani AI and Google Gemini")