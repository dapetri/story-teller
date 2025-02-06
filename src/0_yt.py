import os
from pytubefix import YouTube


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=n_Dv4JMiwK8"
    fn = "minecraft.mp4"
    fp = os.path.join("src", "res", "vid")
    os.makedirs(fp, exist_ok=True)
    YouTube(url).streams.filter(res="1080p").first().download(
        output_path=fp, filename=fn
    )
