from instagrapi import Client
import os

try:
    print("Initializing bot...")
    cl = Client()
    
    # Load your verified session
    if os.path.exists("session.json"):
        cl.load_settings("session.json")
        print("✅ Session loaded successfully")
    else:
        print("❌ session.json not found!")
        exit()

    # Upload the video
    print("Attempting upload...")
    media = cl.video_upload(
        path="video.mp4",
        caption="Uploaded from iPad via GitHub Actions 🚀 #macbook #coding"
    )
    print(f"✅ Video Uploaded! Media Code: {media.code}")

except Exception as e:
    print(f"❌ Error: {e}")
