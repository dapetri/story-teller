import os
from pathlib import Path

from openai import OpenAI

# Set up directories and paths
output_dir = Path(__file__).parent

fp = max(Path("src/res/txt").glob('*.txt'), key=lambda x: x.stat().st_mtime)

with open(fp, 'r', encoding='utf-8') as f:
    story_text = f.read()

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

output_dir = Path("src/res/mp3")
output_dir.mkdir(parents=True, exist_ok=True) 

speech_file_path = output_dir / f"{fp.stem}.mp3"

### TTS ###
with client.audio.speech.with_streaming_response.create(
    model="tts-1",
    voice="onyx",
    speed=0.9,
    input=story_text,
) as response:
    response.stream_to_file(speech_file_path)
### End TTS ###
