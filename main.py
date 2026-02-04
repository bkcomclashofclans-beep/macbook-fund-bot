from instagrapi import Client
from datetime import date
import os

# --- SETTINGS ---
# Change this to TODAY'S date (Year, Month, Day) to start at Day 1
START_DATE = date(2026, 2, 4) 
# ----------------

try:
    # 1. Calculate the Day Number
    today = date.today()
    day_count = (today - START_DATE).days + 1
    
    # 2. Build the Caption
    caption_text = (
        f"Day {day_count} of posting via GitHub Actions 🚀\n\n"
        f"Follow for more! @MacBookm4daily\n\n"
        f".\n.\n.\n"
        f"#day{day_count} #trending #viral #fyp #explorepage #instagram #daily #challenge "
        f"#reels #reelsinstagram #tech #coding #python #bot #automation #macbook "
        f"#kerala #india #programmers #developer #grind #motivation #foryou"
    )

    print(f"generated caption: {caption_text}")

    # 3. Login
    print("Initializing bot...")
    cl = Client()
    
    if os.path.exists("session.json"):
        cl.load_settings("session.json")
        # Initialize the client with the session settings
        cl.login_by_sessionid(cl.request_session.cookies['sessionid']) 
        print("✅ Session loaded successfully")
    else:
        print("❌ session.json not found!")
        exit()

    # 4. Upload
    print("Uploading video...")
    media = cl.video_upload(
        path="video.mp4",
        caption=caption_text
    )
    print(f"✅ Video Uploaded! Media Code: {media.code}")

except Exception as e:
    print(f"❌ Error: {e}")

