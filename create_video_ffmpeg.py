import subprocess

image = "background.jpg"
audio = "voice.mp3"
output = "final_news_video.mp4"

cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-i", image,
    "-i", audio,

    # ✅ make width/height even for libx264
    "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2,format=yuv420p",

    "-c:v", "libx264",
    "-tune", "stillimage",
    "-r", "30",

    "-c:a", "aac",
    "-b:a", "128k",
    "-shortest",
    output
]

subprocess.run(cmd, check=True)
print("✅ final_news_video.mp4 created successfully")
