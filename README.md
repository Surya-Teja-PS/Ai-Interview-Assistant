# AI Interview Assistant 🎙️🤖

An interactive, web-based AI Interview Assistant that conducts real-time, voice-to-voice technical interviews. Powered by advanced Large Language Models and state-of-the-art voice processing, this application dynamically adapts to candidate responses and provides detailed, actionable feedback at the end of the session.

## 🌟 Features

* **Real-Time Voice Interaction:** Seamless integration of Speech-to-Text (AssemblyAI) and Text-to-Speech (Murf AI) for a natural, conversational interview experience.
* **Adaptive AI Interviewer:** Powered by Google Gemini and LangChain, the AI ("Natalie") listens to your actual answers, acknowledges them, and dynamically formulates the next question.
* **Multiple Technical Subjects:** Practice interviews across various domains including Python, Generative AI, HTML, CSS, and general English/Self-Introductions.
* **Comprehensive Feedback:** Automatically generates a detailed JSON-structured feedback report at the end of the interview, highlighting strengths, candidate scores, and specific areas for improvement based on the conversation history.
* **Modern UI/UX:** A clean, responsive interface built with Tailwind CSS, featuring visual audio-recording cues and clean data presentation.

## 🏗️ Architecture

The project follows a standard Client-Server architecture:
* **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript (`index.html`, `index.js`). Handles UI rendering, browser microphone access, and API communication with the local server.
* **Backend:** Python, Flask (`app.py`). Securely manages API keys, processes audio files, orchestrates the LangChain agent memory, and streams audio back to the client.

## 🛠️ Tech Stack

* **Backend Framework:** Python / Flask
* **AI & LLM Orchestration:** LangChain / LangGraph
* **Generative AI:** Google Gemini (gemini-3.6-flash)
* **Speech-to-Text (STT):** AssemblyAI (Universal-3.5-Pro)
* **Text-to-Speech (TTS):** Murf AI
* **Frontend Design:** Tailwind CSS

## 🚀 Getting Started

### Prerequisites
You will need Python 3.x installed on your machine, along with active API keys for the following services:
* [Google Gemini API](https://aistudio.google.com/)
* [AssemblyAI API](https://www.assemblyai.com/)
* [Murf AI API](https://murf.ai/)

### Installation

**1. Clone the repository**
```bash
git clone [https://github.com/YOUR-USERNAME/ai-interview-assistant.git](https://github.com/YOUR-USERNAME/ai-interview-assistant.git)
cd ai-interview-assistant

2. Install dependencies:
pip install -r requirements.txt

3. Configure Environment Variables
Create a .env file in the root directory and securely add your API keys:

GOOGLE_API_KEY="your_google_gemini_api_key"
MURF_API_KEY="your_murf_api_key"
ASSEMBLYAI_API_KEY="your_assemblyai_api_key"

4. Start the Backend Server:
python app.py
The Flask server will start running at http://127.0.0.1:5000.

5. Launch the Frontend
Open the index.html file in your web browser. (If using VS Code, you can use the "Live Server" extension for the best experience).

💡 How to Use
Open the application in your browser.

Select a topic from the left sidebar (e.g., Python, Generative AI).

Click Start Interview and ensure your browser has microphone permissions.

Listen to the AI's question, click the microphone button to record your response, and click stop when finished.

Submit your answer. The AI will process it and ask the next sequential question.

After 5 questions, the interview will conclude. Click Get Feedback to receive your final score and review.

# AI Interview Assistant 🎙️🤖

![Interview Screen](Screenshot%202026-07-29%20162550.png)

![Feedback Screen](Screenshot%202026-07-29%20162603.png)

An interactive, web-based AI Interview Assistant that conducts real-time, voice-to-voice technical interviews. Powered by advanced Large Language Models and state-of-the-art voice processing, this application dynamically adapts to candidate responses and provides detailed, actionable feedback at the end of the session.
