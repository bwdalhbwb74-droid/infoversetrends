import os
import time
import requests

TOKEN = os.getenv(“TELEGRAM_TOKEN”)

offset = 0

print(“Publisher Started”)

while True:
try:
r = requests.get(
f”https://api.telegram.org/bot{TOKEN}/getUpdates”,
params={
“offset”: offset,
“timeout”: 30
}
).json()

    for update in r.get("result", []):
        offset = update["update_id"] + 1
        if "message" not in update:
            continue
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")
        if text == "/start":
            requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                data={
                    "chat_id": chat_id,
                    "text": "🚀 InfoVerse Publisher Ready"
                }
            )
        elif text == "1":
            requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                data={
                    "chat_id": chat_id,
                    "text": "تم اختيار المقال رقم 1"
                }
            )
        else:
            requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                data={
                    "chat_id": chat_id,
                    "text": f"وصلت الرسالة: {text}"
                }
            )
except Exception as e:
    print(e)
time.sleep(2)
