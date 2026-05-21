from flask import Flask, request, jsonify
from faster_whisper import WhisperModel
import os

app = Flask(__name__)

model = WhisperModel("base")

@app.route('/transcribe', methods=['POST'])
def transcribe():

    audio = request.files['file']

    path = "temp_audio.ogg"
    audio.save(path)

    segments, info = model.transcribe(path)

    text = ""

    for segment in segments:
        text += segment.text + " "

    os.remove(path)

    return jsonify({
        "text": text.strip()
    })

app.run(host="0.0.0.0", port=5000)