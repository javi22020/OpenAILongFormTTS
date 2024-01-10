import openai
from functions import divide_text
client = openai.OpenAI()

def generate_audio(text: str):
    audio = bytes()
    chunks = divide_text(text, 4096)
    for chunk in chunks:
        audio += client.audio.speech.create(
            input=chunk,
            voice="nova",
            model="tts-1"
        ).content
    with (open("audio.mp3", "wb")) as f:
        f.write(audio)

if __name__ == "__main__":
    generate_audio(open("text.txt", "r", encoding="utf-8").read())