from moviepy.editor import *
from PIL import Image

# Load audio
audio = AudioFileClip("voice.mp3")

# Load background image
image = ImageClip("background.jpg").set_duration(audio.duration)

# Read headline
with open("news_title.txt", "r", encoding="utf-8") as f:
    title = f.read()

# Add text overlay
txt = TextClip(
    title,
    fontsize=36,
    color="white",
    size=image.size,
    method="caption"
).set_position("center").set_duration(audio.duration)

# Combine everything
video = CompositeVideoClip([image, txt])
video = video.set_audio(audio)

# Export video
video.write_videofile("final_news_video.mp4", fps=24)

print("✅ final_news_video.mp4 created")
