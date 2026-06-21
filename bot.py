import requests

TOKEN = "8763023216:AAGTxJFJD2dnMtBHirSdx_fMhpyszuOkmS0"
CHAT_ID = "7330431242"

message = "🚀 تم تشغيل InfoVerse Trends Bot بنجاح"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})

print("Message Sent")
