from openai import OpenAI
import requests

# Initialize OpenAI client
openai_client = OpenAI()

# --- SPEECH TO TEXT ---
def speech_to_text(audio_binary):
    base_url = 'https://sn-watson-stt.labs.skills.network'
    api_url = base_url + '/speech-to-text/api/v1/recognize'
    params = {'model': 'en-US_Multimedia'}

    response = requests.post(api_url, params=params, data=audio_binary).json()

    text = None
    if bool(response.get('results')):
        print('speech to text response:', response)
        text = response.get('results').pop().get('alternatives').pop().get('transcript')
        print('recognized text: ', text)

    return text


# --- TEXT TO SPEECH ---
def text_to_speech(text, voice=""):
    # Set up Watson Text-to-Speech HTTP API URL
    base_url = 'https://sn-watson-tts.labs.skills.network'
    api_url = base_url + '/text-to-speech/api/v1/synthesize?output=output_text.wav'

    # Add voice parameter if user selects a specific one
    if voice != "" and voice != "default":
        api_url += "&voice=" + voice

    # Set headers for HTTP request
    headers = {
        'Accept': 'audio/wav',
        'Content-Type': 'application/json',
    }

    # Set body of HTTP request
    json_data = {'text': text}

    # Send POST request to Watson TTS service
    response = requests.post(api_url, headers=headers, json=json_data)
    print('text to speech response:', response)
    return response.content


# --- OPENAI MESSAGE PROCESSOR ---
def openai_process_message(user_message):
    prompt = (
        "Act like a personal assistant. You can respond to questions, translate sentences, "
        "summarize news, and give recommendations. Keep responses concise - 2 to 3 sentences maximum."
    )

    openai_response = openai_client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_message}
        ],
        max_completion_tokens=1000
    )

    print("openai response:", openai_response)
    response_text = openai_response.choices[0].message.content
    return response_text
