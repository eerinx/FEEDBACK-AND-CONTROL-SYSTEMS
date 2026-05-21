from faster_whisper import WhisperModel
import sys

audio_path = sys.argv[1]

model = WhisperModel("base")

segments, info = model.transcribe(audio_path)

text = ""

for segment in segments:
    text += segment.text + " "

print(text.strip())