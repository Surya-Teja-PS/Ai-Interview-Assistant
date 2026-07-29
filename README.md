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
"```bash"
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

The 30-Second Elevator Pitch
Start with the big picture. When a manager asks, "Tell me about this AI Interview Assistant," this is your opening script:

"The traditional hiring process is incredibly slow and often biased, so I wanted to build a solution that could scale the initial screening phase. I architected a completely autonomous AI interviewer. It doesn't just read questions off a screen; it actually holds a real-time, two-way vocal conversation with the candidate, adapts to their answers, and instantly generates an objective performance report when the interview ends."

How to Explain the Tech in Simple Terms:
Use the "Brain, Ears/Mouth, and Infrastructure" analogy:

The Brain (LangChain & Gemini 1.5): "I didn't want a bot that just asked robotic questions. I engineered the logic so the system actually 'listens' to the context of the conversation. If a candidate gives a weak answer, the AI remembers it and dynamically generates a smart follow-up question to dig deeper."
The Ears & Mouth (AssemblyAI & Murf AI): "I wanted the user experience to be completely hands-free and natural. I integrated audio pipelines so the system instantly converts the candidate's speech to text, processes the logic, and speaks back to them with a human-like voice."
The Infrastructure (Flask & Render): "To prove this wasn't just a local experiment on my laptop, I built a robust backend and deployed it to the cloud. It is a live, fully functional product that can handle data streams without crashing."
The "Dedication & Hard Work" Angle:
"What I am most proud of with this project is the learning curve. Balancing my core engineering coursework with teaching myself modern software architecture, cloud deployment, and API integrations took a lot of late nights. I had to independently research and troubleshoot complex data streaming issues to get the audio latency down to near-zero, but seeing the live application run flawlessly made the effort entirely worth it."
1. Start with the Problem (The "Why")
Managers want to know that you understand the business value of what you built. Start by explaining why normal AI isn't good enough for an interview:

Most conversational AI bots today are stuck in a simple loop: a user sends a message, the agent responds, and the loop repeats.

This linear approach works for simple Q&A, but it crumbles when faced with real-world conversational complexity.

Meaningful conversations are not linear; they branch, loop, and adapt based on user input.

2. Explain Your AI Logic (The "How" in Simple Terms)
Next, explain the technology using the concept of "memory and state" without getting lost in the code.

To build an agent that is truly conversational and not just reactive, I engineered the system as an event-driven state machine.

I used LangGraph, a library built on top of LangChain, to manage this logic.

Rather than just reacting to the last thing the user said, the system uses memory to maintain context and act as the living record of the agent's reasoning.

By adding short-term memory as a part of the agent's state, the application tracks multi-turn conversations perfectly.

This memory architecture transforms a simple text-in-text-out model into a coherent assistant that can track complex dialogue.

Put it simply for the manager: "In plain English, the AI doesn't just read off a list of questions. It 'remembers' exactly what the candidate said three questions ago, evaluates their reasoning in real-time, and dynamically changes its next question to dig deeper into their weaknesses or strengths."

3. Highlight Your Dedication (The Hustle)
This is where you lock in the offer. You need to frame this technical achievement against the backdrop of your daily life.

Moving from simple automated bots to true intelligent interaction is a challenge of robust software architecture.

Mastering advanced AI architecture, state management, and memory systems is entirely self-taught outside of my rigorous Civil Engineering curriculum at IIT Madras.

Balancing structural design labs and heavy coursework while independently researching how to architect sophisticated conversational systems took immense discipline.

I pushed through complex debugging and late nights because I was determined to transform this AI from a simple tool into an intelligent partner.


