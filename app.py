from google.cloud import texttospeech
from flask import Flask, send_file
from google.oauth2.service_account import Credentials
from flask_cors import CORS
import time
app = Flask(__name__)
CORS(app)
@app.route('/')
def hello_world():
    key_path = "/home/user/cbot/scripts/deepakkumar.json"  # gcp project texttospeech api enabled can be set in config.py
    credentials = Credentials.from_service_account_file(key_path)
    # Instantiates a client
    client = texttospeech.TextToSpeechClient(credentials=credentials)
    t1 = time.time()
    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text="Hello, my dog is cute. Is it okay? Goods and Services Tax Act (GST), pegged as a major tax reform post-independence, has already been introduced by the Government of India and is likely to be implemented from 1 July 2017. This will subsume most of the indirect taxes (such as VAT, excise, service tax etc.) levied by the Centre and State governments. GST is applicable on all goods and services except for supply of alcohol, petrol, electricity, etc. The new tax regime aims to bring efficiency in the procurement process and create a ‘single market’ to enable nothing.")  # Text obtained by model

    # Build the voice request with Indian English and a female voice
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-IN", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        name="en-IN-Wavenet-A"  # Any name from "https://cloud.google.com/text-to-speech/docs/voices"
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    print("---->",time.time()-t1)
    # The response's audio_content is binary.
    with open("output_tts.mp3", "wb") as out:
        out.write(response.audio_content)

    return send_file("output_tts.mp3")

if __name__ == '__main__':
    app.run(debug=True)

