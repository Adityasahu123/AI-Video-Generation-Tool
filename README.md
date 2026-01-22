# AI Video Generation Tool – Trending News to Short Video 🎥📰

This project is a prototype tool that:
1) fetches a trending news topic/article,  
2) generates a short script,  
3) converts the script into voice (TTS), and  
4) creates a 30–60 sec video with background image + audio (and optional text overlay).

✅ Designed for quick demo/prototype submission for internship assignment.

---

## ✅ Output Files (Generated)
After running the pipeline, you will get:
- `news_title.txt` → fetched trending article title  
- `news_text.txt` → fetched article text/preview  
- `script.txt` → generated narration script  
- `voice.mp3` → voice narration audio  
- `final_news_video.mp4` → final video output  
- `AI_News_Video_Assignment_Report.pdf` → report (steps + explanation)

---

## 📁 Project Structure
AI-Video-Generation-Tool/
│── fetch_news.py
│── generate_script.py
│── text_to_voice.py
│── create_video_ffmpeg.py
│── background.jpg
│── news_title.txt
│── news_text.txt
│── script.txt
│── voice.mp3
│── final_news_video.mp4
│── AI_News_Video_Assignment_Report.pdf


---

## ⚙️ Requirements (Windows)
### 1) Python
- Python 3.10+ recommended  
Check:
```bash
python --version
2) Install Python Packages
Run inside project folder:

pip install requests beautifulsoup4 gtts
3) Install FFmpeg (Required for Video)
Option A (Recommended): via Winget

winget install --id Gyan.FFmpeg
Close PowerShell and open again, then check:

ffmpeg -version
▶️ How to Run (Full Pipeline)
Open PowerShell in the project folder and run these commands in order:

Step 1 — Fetch Trending News
python fetch_news.py
✅ Creates: news_title.txt, news_text.txt

Step 2 — Generate Script
python generate_script.py
✅ Creates: script.txt

Step 3 — Convert Script to Voice (TTS)
python text_to_voice.py
✅ Creates: voice.mp3

Step 4 — Create Final Video
python create_video_ffmpeg.py
✅ Creates: final_news_video.mp4

🎬 Result
Final output video:

final_news_video.mp4 (30–60 seconds)

Contains background visual + narration audio
(Optional: can be extended to add text overlays and multiple images.)

🧠 Architecture (High Level)
Scraping / RSS feed → get trending news

Script generation → short narration text

TTS → voice mp3

FFmpeg → merges image + voice into mp4

🔧 Notes / Troubleshooting
If FFmpeg is not found
Close the terminal and open PowerShell again, then run:

ffmpeg -version
If video fails due to image size (width must be divisible by 2)
Replace background.jpg with a normal 1280x720 image, OR resize it.

✅ Deliverables Included
Source code (.py)

Generated video (final_news_video.mp4)

Generated assets (news_*.txt, script.txt, voice.mp3)

Report (AI_News_Video_Assignment_Report.pdf)

Author
Aditya Sahu
