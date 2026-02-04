from instagrapi import Client
from datetime import date
import os
import time
import random
from urllib.parse import unquote

# --- SETTINGS ---
START_DATE = date(2026, 2, 4) 

# YOUR SESSION ID (Hardcoded so it cannot fail)
SESSION_ID = "80121861323%3AFSMEyXAUIwrhFr%3A6%3AAYi7h1W-76-NuppibxvebPa7-5nFSQ4W4YolMf1tbQ"
# ----------------

try:
    # 1. MAGIC FIX (Bypass Spam Filter)
    print("✨ Applying magic fix...")
    with open("video.mp4", "ab") as f:
        f.write(os.urandom(1))

    # 2. SHORT DELAY (Testing Mode: 1 min)
    print("⏳ Waiting 1 minute...")
    time.sleep(60)

    # 3. CAPTION
    today = date.today()
    day_count = (today - START_DATE).days + 1
    caption = (
        f"Day {day_count}: The Daily Grind 🚀\n\n"
        f"Consistency is key. Follow @MacBookm4daily\n\n"
        f"#day{day_count} #macbookfund #grind #kerala #india #coding #motivation"
    )

    # 4. DIRECT LOGIN
    print("Logging in...")
    cl = Client()
    
    # Decrypt the ID and use it directly
    decoded_session = unquote(SESSION_ID)
    cl.login_by_sessionid(decoded_session)
    print("✅ Login Successful")

    # 5. UPLOAD
    print("Uploading video...")
    media = cl.video_upload(path="video.mp4", caption=caption)
    
    # 6. LINK
    print(f"✅ DONE! Watch here: https://www.instagram.com/reel/{media.code}/")

except Exception as e:
    print(f"❌ Error: {e}")
