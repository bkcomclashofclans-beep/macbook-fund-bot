from instagrapi import Client
from datetime import date
import os
import time
import random

# --- SETTINGS ---
START_DATE = date(2026, 2, 4) 
# ----------------

try:
    # 1. THE MAGIC TRICK (Bypass Spam Filter)
    print("✨ Applying magic fix to video...")
    with open("video.mp4", "ab") as f:
        f.write(os.urandom(1))

    # 2. Human Delay
    delay = random.randint(10, 60)
    print(f"⏳ Waiting {delay} minutes to look human...")
    time.sleep(delay * 60)

    # 3. Calculate Day
    today = date.today()
    day_count = (today - START_DATE).days + 1
    
    # 4. Caption
    caption_text = (
        f"Day {day_count}: The Daily Grind 🚀\n\n"
        f"Consistency is everything. Follow @MacBookm4daily\n\n"
        f".\n.\n.\n"
        f"#day{day_count} #macbookfund #grind #kerala #india #coding #motivation #viral"
    )

    # 5. Login
    print("Logging in...")
    cl = Client()
    if os.path.exists("session.json"):
        cl.load_settings("session.json")
        cl.login_by_sessionid(cl.request_session.cookies['sessionid']) 
    
    # 6. Upload
    print("Uploading video...")
    media = cl.video_upload(
        path="video.mp4",
        caption=caption_text
    )
    
    # 7. GENERATE LINK
    shortcode = media.code
    url = f"https://www.instagram.com/reel/{shortcode}/"
    
    print(f"✅ Success! Video is live.")
    print(f"🔗 CLICK HERE TO WATCH: {url}")

except Exception as e:
    print(f"❌ Error: {e}")
