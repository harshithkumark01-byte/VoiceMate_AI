# 🎙️ VoiceMate AI
### Intelligent Multilingual Customer Support Assistant

VoiceMate AI is a Python-based multilingual voice assistant that helps users communicate with an AI-powered customer support system using natural speech.

Users can record their voice, convert speech into text, receive intelligent responses and listen to AI-generated voice replies.

## 🚀 Features

- Speech-to-Text using Gnani AI Prisma.
- AI-powered response generation using Google Gemini.
- Text-to-Speech using Gnani AI Timbre.
- Multilingual language selection.
- Voice recording and playback.
- Text-based voice generation.
- Interactive Streamlit interface.

## 🌐 Supported Languages

- English
- Kannada
- Hindi
- Tamil
- Telugu

## 🛠️ Technologies Used

- Python
- Streamlit
- Gnani AI Prisma
- Gnani AI Timbre
- Google Gemini API
- Requests
- Python Dotenv

## ⚙️ Project Structure

```text
VoiceMate_AI/
├── app.py
├── speech_to_text.py
├── text_to_speech.py
├── ai_assistant.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

## 💻 Installation and Setup

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Open the project folder:

```bash
cd VoiceMate_AI
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate it on Windows:

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Create a `.env` file in the project folder and configure your API keys:

```env
GNANI_API_KEY=your_gnani_api_key
GEMINI_API_KEY=your_gemini_api_key
```

Never upload your actual API keys to GitHub.

7. Run the application:

```bash
streamlit run app.py
```

## 🔄 How It Works

1. The user selects a preferred language.
2. The user records a voice message.
3. Gnani AI Prisma converts speech into text.
4. Google Gemini generates an intelligent response.
5. Gnani AI Timbre converts the response into speech.
6. The user listens to the generated voice response.

## 🎯 Objective

The objective of VoiceMate AI is to demonstrate how speech recognition, generative AI and speech synthesis can work together to create an accessible multilingual customer support experience.

## 👨‍💻 Developer

**Harshith Kumar K**

Project developed for the Great Indian AI Internship Challenge.

## 🙏 Acknowledgements

- Gnani AI
- Google Gemini
- Streamlit