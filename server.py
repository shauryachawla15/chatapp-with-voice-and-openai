from flask import Flask, render_template, request
from flask_cors import CORS
from worker import speech_to_text, text_to_speech, openai_process_message
import os
import json
import base64

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)


# --- INDEX ROUTE (Frontend UI) ---
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# --- SPEECH TO TEXT ROUTE ---
@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    print("processing speech-to-text")

    # Get the user's speech (audio binary)
    audio_binary = request.data

    # Call the Watson STT function
    text = speech_to_text(audio_binary)

    # Return as JSON response
    response = app.response_class(
        response=json.dumps({'text': text}),
        status=200,
        mimetype='application/json'
    )

    print(response)
    print(response.data)
    return response


# --- PROCESS MESSAGE ROUTE ---
@app.route('/process-message', methods=['POST'])
def process_message_route():
    user_message = request.json['userMessage']  # user text
    print('user_message:', user_message)

    voice = request.json['voice']  # user’s selected voice
    print('voice:', voice)

    # Step 1: Send text to OpenAI for processing
    openai_response_text = openai_process_message(user_message)

    # Step 2: Clean response (remove blank lines)
    openai_response_text = os.linesep.join([s for s in openai_response_text.splitlines() if s])

    # Step 3: Convert text to speech (Watson TTS)
    openai_response_speech = text_to_speech(openai_response_text, voice)

    # Step 4: Encode audio data to Base64 so JSON can handle it
    openai_response_speech = base64.b64encode(openai_response_speech).decode('utf-8')

    # Step 5: Send JSON response with both text + audio
    response = app.response_class(
        response=json.dumps({
            "openaiResponseText": openai_response_text,
            "openaiResponseSpeech": openai_response_speech
        }),
        status=200,
        mimetype='application/json'
    )

    print(response)
    return response


# --- START SERVER ---
if __name__ == '__main__':
    print("✅ Voice Assistant Server is Running!")
    print("Visit: http://127.0.0.1:8080 or http://localhost:8080")
    print("Available routes: /, /speech-to-text, /process-message")
    app.run(host='0.0.0.0', port=8080, debug=True)
