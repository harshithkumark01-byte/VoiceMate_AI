import streamlit as st
import os
import tempfile
from dotenv import load_dotenv

from speech_to_text import transcribe_audio
from text_to_speech import generate_speech
from ai_assistant import generate_response


# ==========================================
# CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="VoiceMate AI",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_dotenv()

GNANI_API_KEY = os.getenv("GNANI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# ==========================================
# SESSION STATE
# ==========================================

if "transcript" not in st.session_state:
    st.session_state.transcript = ""

if "ai_reply" not in st.session_state:
    st.session_state.ai_reply = ""

if "conversation" not in st.session_state:
    st.session_state.conversation = []


# ==========================================
# LANGUAGE CONFIGURATION
# ==========================================

language_codes = {
    "English": "en-IN",
    "Kannada": "kn-IN",
    "Hindi": "hi-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN"
}


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: #FFFFFF;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #FFFFFF;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 17px;
    color: #A0A7B4;
    margin-bottom: 25px;
}

.section-title {
    font-size: 23px;
    font-weight: 700;
    color: #FFFFFF;
    margin-top: 15px;
    margin-bottom: 15px;
}

.status-card {
    background-color: #1B2230;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #303846;
    text-align: center;
}

.status-label {
    color: #A0A7B4;
    font-size: 14px;
}

.status-value {
    color: #FFFFFF;
    font-size: 18px;
    font-weight: 700;
}

.feature-card {
    background-color: #1B2230;
    padding: 22px;
    border-radius: 14px;
    border: 1px solid #303846;
    margin-bottom: 15px;
}

.feature-card h3 {
    color: #FFFFFF;
}

.feature-card p {
    color: #A0A7B4;
}

div.stButton > button {
    background-color: #635BFF;
    color: white;
    border-radius: 9px;
    border: none;
    padding: 10px 20px;
    font-weight: 600;
}

div.stButton > button:hover {
    background-color: #5048D8;
    color: white;
    border: none;
}

[data-testid="stSidebar"] {
    background-color: #151A23;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF;
}

hr {
    border-color: #303846;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("# 🎙️ VoiceMate AI")

    st.caption("Your Multilingual AI Assistant")

    st.divider()

    st.markdown("### 🔌 API CONNECTIONS")

    if GNANI_API_KEY:
        st.success("Gnani AI Connected")
    else:
        st.error("Gnani API Not Configured")

    if GEMINI_API_KEY:
        st.success("Gemini AI Connected")
    else:
        st.error("Gemini API Not Configured")

    st.divider()

    st.markdown("### 🌐 SELECT LANGUAGE")

    language = st.selectbox(
        "Choose your language",
        list(language_codes.keys())
    )

    st.info(f"Selected: {language}")

    st.divider()

    if st.button("🗑️ Clear Conversation", use_container_width=True):

        st.session_state.transcript = ""
        st.session_state.ai_reply = ""
        st.session_state.conversation = []

        st.rerun()

    st.markdown("---")

    st.caption("VoiceMate AI | Internship Project")


# ==========================================
# MAIN HEADER
# ==========================================

st.markdown(
    '<div class="main-title">🎙️ VoiceMate AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Intelligent Multilingual AI Customer Support Assistant'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ==========================================
# API STATUS
# ==========================================

st.markdown(
    '<div class="section-title">⚡ System Overview</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="status-card">
        <div class="status-label">Speech Recognition</div>
        <div class="status-value">🎤 Gnani AI</div>
    </div>
    """, unsafe_allow_html=True)

    if GNANI_API_KEY:
        st.success("Connected")
    else:
        st.error("Not Connected")


with col2:

    st.markdown("""
    <div class="status-card">
        <div class="status-label">AI Intelligence</div>
        <div class="status-value">🤖 Gemini AI</div>
    </div>
    """, unsafe_allow_html=True)

    if GEMINI_API_KEY:
        st.success("Connected")
    else:
        st.error("Not Connected")


with col3:

    st.markdown("""
    <div class="status-card">
        <div class="status-label">Voice Generation</div>
        <div class="status-value">🔊 Gnani AI</div>
    </div>
    """, unsafe_allow_html=True)

    if GNANI_API_KEY:
        st.success("Connected")
    else:
        st.error("Not Connected")


st.divider()


# ==========================================
# VOICE ASSISTANT
# ==========================================

st.markdown(
    '<div class="section-title">🎤 Talk to VoiceMate</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="feature-card">
    <h3>Speak naturally. Get intelligent answers.</h3>
    <p>
        Record your voice and VoiceMate AI will recognize your speech,
        understand your request and generate an intelligent response.
    </p>
</div>
""", unsafe_allow_html=True)


audio = st.audio_input("🎙️ Click to record your voice")

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

            # Speech to Text

            with st.spinner("🎧 Recognizing your speech..."):

                transcript = transcribe_audio(
                    audio_path,
                    language_codes[language]
                )

            st.session_state.transcript = transcript

            # Gemini AI

            with st.spinner("🤖 Gemini is preparing your response..."):

                ai_reply = generate_response(transcript)

            st.session_state.ai_reply = ai_reply

            st.session_state.conversation.append({
                "user": transcript,
                "assistant": ai_reply
            })

            st.success("Your voice request was processed successfully!")

        except Exception as e:

            st.error(f"Processing failed: {e}")

        finally:

            if audio_path and os.path.exists(audio_path):
                os.remove(audio_path)


# ==========================================
# CONVERSATION DISPLAY
# ==========================================

if st.session_state.transcript:

    st.divider()

    st.markdown(
        '<div class="section-title">💬 Conversation</div>',
        unsafe_allow_html=True
    )

    st.markdown("### 👤 You")

    st.info(st.session_state.transcript)

    st.markdown("### 🤖 VoiceMate AI")

    st.success(st.session_state.ai_reply)

    if st.button("🔊 Listen to AI Response"):

        try:

            with st.spinner("Generating AI voice..."):

                audio_output = generate_speech(
                    st.session_state.ai_reply,
                    language=language_codes[language]
                )

            st.audio(audio_output, format="audio/wav")

        except Exception as e:

            st.error(f"Voice generation failed: {e}")


# ==========================================
# MANUAL AI CHAT
# ==========================================

st.divider()

st.markdown(
    '<div class="section-title">🤖 Ask VoiceMate AI</div>',
    unsafe_allow_html=True
)

st.write(
    "You can also interact with VoiceMate AI using text "
    "without recording your voice."
)

user_question = st.text_area(
    "Enter your question",
    placeholder="Example: How can I reset my account password?"
)

if st.button("🚀 Generate AI Response"):

    if user_question.strip():

        try:

            with st.spinner("Gemini is thinking..."):

                answer = generate_response(user_question)

            st.session_state.ai_reply = answer
            st.session_state.transcript = user_question

            st.session_state.conversation.append({
                "user": user_question,
                "assistant": answer
            })

            st.success("Response generated successfully!")

            st.markdown("### 🤖 VoiceMate AI Response")

            st.write(answer)

        except Exception as e:

            st.error(f"Gemini error: {e}")

    else:

        st.warning("Please enter a question.")


# ==========================================
# MANUAL TEXT TO SPEECH
# ==========================================

st.divider()

st.markdown(
    '<div class="section-title">🔊 Text to Speech</div>',
    unsafe_allow_html=True
)

st.write(
    "Convert any text into natural AI-generated speech."
)

response_text = st.text_area(
    "Enter text to convert into speech",
    placeholder="Hello! Welcome to VoiceMate AI."
)

if st.button("🎵 Generate Voice"):

    if response_text.strip():

        try:

            with st.spinner("Generating voice..."):

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


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown(
    """
    <div style="text-align:center; color:#A0A7B4; padding:20px;">

        <h4>🎙️ VoiceMate AI</h4>

        <p>
            Multilingual AI Customer Support Assistant
        </p>

        <p>
            Powered by Gnani AI | Google Gemini | Streamlit
        </p>

        <small>Internship Project | 2026</small>

    </div>
    """,
    unsafe_allow_html=True
)