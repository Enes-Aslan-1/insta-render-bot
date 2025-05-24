from instagrapi import Client
from datetime import datetime
import os
import pathlib

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")
SESSION_FILE = "session.json"
VIDEO_PATH = "video.mp4"
CAPTION = f"Günün videosu! Bugün: {datetime.now().strftime('%d.%m.%Y')} #otomasyon"

def login_with_session():
    cl = Client()
    if pathlib.Path(SESSION_FILE).exists():
        try:
            cl.load_settings(SESSION_FILE)
            cl.login(USERNAME, PASSWORD)
            print("🔐 Session ile giriş başarılı")
        except Exception as e:
            print(f"⚠️ Session ile giriş başarısız: {e}")
            cl.set_settings({})
            cl.login(USERNAME, PASSWORD)
            cl.dump_settings(SESSION_FILE)
            print("✅ Yeni session kaydedildi")
    else:
        cl.login(USERNAME, PASSWORD)
        cl.dump_settings(SESSION_FILE)
        print("✅ Session ilk defa oluşturuldu")
    return cl

def main():
    cl = login_with_session()
    cl.video_upload(VIDEO_PATH, CAPTION)
    print("✅ Video yüklendi")

if __name__ == "__main__":
    main()
