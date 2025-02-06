import os
from pathlib import Path

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def get_mp3():
    fp = max(Path("src/res/txt").glob("*.txt"), key=lambda x: x.stat().st_mtime)

    with open(fp, "r", encoding="utf-8") as f:
        story_text = f.read()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    output_dir = Path("src/res/mp3")
    output_dir.mkdir(parents=True, exist_ok=True)

    speech_file_path = output_dir / f"{fp.stem}.mp3"

    ### TTS ###
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="onyx",
        input=story_text,
    ) as response:
        response.stream_to_file(speech_file_path)
    ### End TTS ###


if __name__ == "__main__":
    get_mp3()
