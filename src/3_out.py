import os
import random

import ffmpeg
from moviepy import AudioFileClip, VideoFileClip


def get_newest_mp3(mp3_dir):
    mp3_files = [f for f in os.listdir(mp3_dir) if f.endswith(".mp3")]
    newest_mp3 = max(
        mp3_files, key=lambda f: os.path.getctime(os.path.join(mp3_dir, f))
    )
    return os.path.join(mp3_dir, newest_mp3)


def create_video_clip_with_audio(video_path, audio_path, output_path):
    # Get audio duration using moviepy
    audio = AudioFileClip(audio_path)
    audio_duration = audio.duration
    audio.close()

    # Get video info using ffmpeg
    probe = ffmpeg.probe(video_path)
    video_duration = float(probe["format"]["duration"])

    if audio_duration > video_duration:
        raise ValueError("Audio duration is longer than video duration")

    # Calculate random start time
    start_time = random.uniform(0, video_duration - audio_duration)

    # Process video with ffmpeg
    stream = ffmpeg.input(video_path, ss=start_time, t=audio_duration)

    # Apply filters for 9:16 ratio at 1080p
    stream = stream.filter("scale", -1, "1080").filter(  # Scale to 1080p height
        "crop", "608", "1080", "(iw-608)/2", "0"
    )  # Crop to 9:16

    # Add audio
    audio_stream = ffmpeg.input(audio_path)

    # Combine and output
    stream = ffmpeg.output(
        stream, audio_stream, output_path, acodec="aac", vcodec="libx264"
    )

    # Run ffmpeg
    ffmpeg.run(stream, overwrite_output=True)


if __name__ == "__main__":
    mp3_dir = "src/res/mp3"
    video_path = "src/res/vid/up.mp4"
    output_dir = "src/res/out"

    newest_mp3 = get_newest_mp3(mp3_dir)
    mp3_filename = os.path.splitext(os.path.basename(newest_mp3))[0]
    output_path = os.path.join(output_dir, f"{mp3_filename}.mp4")

    os.makedirs(output_dir, exist_ok=True)
    create_video_clip_with_audio(video_path, newest_mp3, output_path)
