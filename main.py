from instagrapi import Client
from datetime import date
import os
import time
import random
from urllib.parse import unquote

# --- SETTINGS ---
START_DATE = date(2026, 2, 4) 
# ----------------

try:
    # 1. MAGIC FIX (Bypass Spam Filter)
    print("✨ Applying magic fix...")
    with open("video.mp4", "ab") as f:
        f.write(os.urandom(1))

    # 2. SHORT DELAY (1 minute for testing)
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

    # 4. MANUAL COOKIE INJECTION (Bypasses the crash)
    print("Injecting cookies...")
    cl = Client()
    
    # We set the cookies directly instead of using the login function
    # (Values taken from your Screenshot #1)
    
    # 1. User ID
    cl.request.cookies.set("ds_user_id", "80121861323", domain=".instagram.com")
    
    # 2. CSRF Token
    cl.request.cookies.set("csrftoken", "0ll1LrZvtudPjAvvB4vERn", domain=".instagram.com")
    
    # 3. Session ID (Decoded)
    raw_session = "80121861323%3AFSMEyXAUIwrhFr%3A6%3AAYi7h1W-76-NuppibxvebPa7-5nFSQ4W4YolMf1tbQ"
    cl.request.cookies.set("sessionid", unquote(raw_session), domain=".instagram.com")

    print("✅ Cookies injected. Attempting upload...")

    # 5. UPLOAD
    media = cl.video_upload(path="video.mp4", caption=caption)
    
    # 6. LINK
    print(f"✅ DONE! Watch here: https://www.instagram.com/reel/{media.code}/")

except Exception as e:
    # This will print the FULL error if something goes wrong
    import traceback
    print(traceback.format_exc())
