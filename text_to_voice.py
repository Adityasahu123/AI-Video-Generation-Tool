from gtts import gTTS

# Read the generated script
with open("script.txt", "r", encoding="utf-8") as f:
    script = f.read().strip()

if len(script) < 50:
    raise Exception("Script too short. Step 2 failed.")

tts = gTTS(text=script, lang="en")
tts.save("voice.mp3")

print("✅ voice.mp3 created successfully")
