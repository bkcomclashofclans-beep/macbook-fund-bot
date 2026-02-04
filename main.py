from instagrapi import Client
from datetime import date
import os
import time
import random
import json

# --- SETTINGS ---
START_DATE = date(2026, 2, 4) 
# ----------------

try:
    # 1. THE MAGIC TRICK (Bypass Spam Filter)
    print("✨ Applying magic fix to video...")
    with open("video.mp4", "ab") as f:
        f.write(os.urandom(1))

    # 2. SHORT HUMAN DELAY (1-10 mins)
    delay = random.randint(1, 10)
    print(f"⏳ Waiting {delay} minutes to look human...")
    time.sleep(delay * 60)

    # 3. CALCULATE DAY
    today = date.today()
    day_count = (today - START_DATE).days + 1
    
    caption_text = (
        f"Day {day_count}: The Daily Grind 🚀\n\n"
        f"Consistency is everything. Follow @MacBookm4daily\n\n"
        f".\n.\n.\n"
        f"#day{day_count} #macbookfund #grind #kerala #india #coding #motivation #viral"
    )

    # 4. ROBUST LOGIN (The Fix)
    print("Logging in...")
    cl = Client()
    
    if os.path.exists("session.json"):
        cl.load_settings("session.json")
        
        # MANUAL FIX: Read the session ID directly from the file
        with open("session.json", "r") as f:
            data = json.load(f)
        
        # Extract sessionid safely
        session_id = data.get("authorization_data", {}).get("sessionid") or data.get("cookies", {}).get("sessionid")
            
        if session_id:
            cl.login_by_sessionid(session_id)
            print("✅ Session loaded and verified")
        else:
            print("❌ Could not find session ID in file")
            exit()
    else:
        print("❌ session.json not found!")
        exit()
    
    # 5. UPLOAD
    print("Uploading video...")
    media = cl.video_upload(
        path="video.mp4",
        caption=caption_text
    )
    
    # 6. GENERATE LINK
    shortcode = media.code
    url = f"https://www.instagram.com/reel/{shortcode}/"
    
    print(f"✅ Success! Video is live.")
    print(f"🔗 CLICK HERE TO WATCH: {url}")

except Exception as e:
    print(f"❌ Error: {e}")
