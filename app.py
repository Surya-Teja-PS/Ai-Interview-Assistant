from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
import assemblyai as aai
import os
import base64
import requests
import tempfile
import json
import ast

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MURF_API_KEY = os.getenv("MURF_API_KEY")
ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
aai.settings.api_key = ASSEMBLYAI_API_KEY

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=GOOGLE_API_KEY
)
checkpointer = InMemorySaver()
agent = create_agent(
    model=model,
    tools=[],
    checkpointer=checkpointer
)

question_count = 0
current_subject = ""
thread_id = "interview_session"

INTERVIEW_PROMPT = """You are Natalie, a friendly and conversational interviewer conducting a natural {subject} interview.

IMPORTANT GUIDELINES:
1. Ask exactly 5 questions total throughout the interview
2. Keep questions SHORT and CRISP (1-2 sentences maximum)
3. ALWAYS reference what the candidate ACTUALLY said in their previous answer - do NOT make up or assume their answers
4. Show genuine interest with brief acknowledgments based on their REAL responses
5. Adapt questions based on their ACTUAL responses - go deeper if they're strong, adjust if uncertain
6. Be warm and conversational but CONCISE
7. No lengthy explanations - just ask clear, direct questions

CRITICAL: Read the conversation history carefully. Only acknowledge what the candidate truly said, not what you think they might have said.

Keep it short, conversational, and adaptive!"""

FEEDBACK_PROMPT = """Based on our complete interview conversation, provide detailed feedback as JSON only:
    {{
    "subject": "<topic>",
    "candidate_score": <1-5>,
    "feedback": "<detailed strengths with specific examples 
    from their ACTUAL answers>",
    "areas_of_improvement": "<constructive suggestions based 
    on gaps you noticed>"
    }}
    Be specific - reference ACTUAL things they said during the interview."""

app = Flask(__name__)
CORS(app, expose_headers=['X-Question-Number', 'X-Interview-Complete'])

# --- HELPER FUNCTION TO CLEAN GEMINI OUTPUT ---
def clean_gemini_text(raw_content):
    if isinstance(raw_content, list):
        return "".join([item.get("text", "") for item in raw_content if isinstance(item, dict)])
    elif isinstance(raw_content, str) and "'text':" in raw_content:
        try:
            parsed = ast.literal_eval(raw_content)
            return "".join([item.get("text", "") for item in parsed if isinstance(item, dict)])
        except:
            return raw_content
    return str(raw_content)

def stream_audio(text):
    BASE_URL = "https://global.api.murf.ai/v1/speech/stream"
    payload = {
        "text": text,
        "voiceId": "en-US-natalie",
        "model": "FALCON",
        "multiNativeLocale": "en-US",
        "sampleRate": 24000,
        "format": "MP3",
    }

    headers = {
        "Content-Type": "application/json",
        "api-key": MURF_API_KEY
    }
    response = requests.post(
        BASE_URL,
        headers=headers,
        data=json.dumps(payload),
        stream=True
    )
    for chunk in response.iter_content(chunk_size=4096):
        if chunk:
            yield base64.b64encode(chunk).decode("utf-8") + "\n"

@app.route("/start-interview", methods=["POST"])
def start_interview():
    global current_subject, question_count, checkpointer, agent
    
    # Fixed empty JSON vulnerability
    data = request.json or {}
    current_subject = data.get("subject", "Python")
    question_count = 1
    
    checkpointer = InMemorySaver()
    agent = create_agent(
        model=model,
        tools=[],
        checkpointer=checkpointer
    )
    config = {"configurable": {"thread_id": thread_id}}
    formatted_prompt = INTERVIEW_PROMPT.format(subject=current_subject)
    
    response = agent.invoke({
        "messages": [
            {"role": "system", "content": formatted_prompt},
            {"role": "user", "content": f"Start the interview with a warm greeting and ask the first question about {current_subject}. Keep it SHORT (1-2 sentences)."}
        ]
    }, config=config)
    
    # Cleaned the question text here
    raw_question = response["messages"][-1].content
    question = clean_gemini_text(raw_question)
    
    print(f"\n[Question {question_count}] {question}")
    return Response(stream_audio(question), mimetype="text/plain")

def speech_to_text(audio_path):
    """Convert audio file to text using AssemblyAI"""
    transcriber = aai.Transcriber()
    config = aai.TranscriptionConfig(
        speech_models=["universal-3-5-pro", "universal-2"],
        language_detection=True, speaker_labels=True,
    )
    transcript = transcriber.transcribe(audio_path, config=config)
    return transcript.text if transcript.text else ""

@app.route("/submit-answer", methods=["POST"])
def submit_answer():
    global question_count
    
    audio_file = request.files["audio"]
    temp_path = tempfile.NamedTemporaryFile(delete=False, suffix=".webm").name
    audio_file.save(temp_path)
    
    answer = speech_to_text(temp_path)
    os.unlink(temp_path)
    
    if not answer or answer.strip() == "":
        answer = "[Candidate provided a verbal response]"
    
    print(f"[Answer {question_count}] {answer}")
    config = {"configurable": {"thread_id": thread_id}}
    agent.invoke({"messages": [{"role": "user", "content": answer}]}, config=config)
    
    if question_count >= 5:
        response = agent.invoke({
            "messages": [{"role": "user", "content": "That was the 5th question. Briefly acknowledge their ACTUAL answer and let them know the interview is complete. Keep it SHORT."}]
        }, config=config)
        
        # Cleaned closing message here
        raw_closing = response["messages"][-1].content
        closing_message = clean_gemini_text(raw_closing)
        
        print(f"\n[Closing] {closing_message}")
        return Response(
            stream_audio(closing_message),
            mimetype='text/plain',
            headers={'X-Interview-Complete': 'true'}
        )
    
    question_count += 1
    prompt = f"""The candidate just answered question {question_count - 1}.

Look at their ACTUAL answer above. Do NOT assume or make up what they said.

Now ask question {question_count} of 5:
1. Briefly acknowledge what they ACTUALLY said (1 sentence) - quote their exact words if needed
2. Ask your next question that builds on their REAL response (1-2 sentences)
3. If they said "I don't know" or gave a wrong answer, acknowledge that and ask something simpler
4. Keep the TOTAL response under 3 sentences

Be conversational but CONCISE. Only reference what they truly said."""
    
    response = agent.invoke({"messages": [{"role": "user", "content": prompt}]}, config=config)
    
    # Cleaned next question here
    raw_question = response["messages"][-1].content
    question = clean_gemini_text(raw_question)
    
    print(f"\n[Question {question_count}] {question}")
    return Response(
        stream_audio(question),
        mimetype='text/plain',
        headers={'X-Question-Number': str(question_count)}
    )

@app.route("/get-feedback", methods=["POST"])
def get_feedback():
    """Generate detailed interview feedback"""
    config = {"configurable": {"thread_id": thread_id}}
    response = agent.invoke({
        "messages": [
        {
            "role": "user", 
            "content": f"{FEEDBACK_PROMPT}\n\nReview our complete {current_subject} interview conversation and provide detailed feedback."
        }
        ]
    }, config=config)
    
    # 1. Get the raw data block
    raw_text = response["messages"][-1].content
    print(f"\n[Feedback Generated Raw]\n{raw_text}\n")
    
    # 2. Extract just the text string using the helper function
    text = clean_gemini_text(raw_text)
    
    # 3. Now strip and parse it safely
    cleaned = text.strip()
    if "```" in cleaned:
        cleaned = cleaned.split("```")[1].replace("json", "").strip()
        
    try:
        feedback = json.loads(cleaned)
    except json.JSONDecodeError as e:
        print(f"JSON Parse Error: {e}")
        feedback = {
            "subject": current_subject,
            "candidate_score": 0,
            "feedback": "There was a slight error formatting your feedback. Please try again!",
            "areas_of_improvement": "No suggestions available."
        }

    return jsonify({"success": True, "feedback": feedback})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
