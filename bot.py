from pytrends.request import TrendReq
import requests

TOKEN = "8763023216:AAGTxJFJD2dnMtBHirSdx_fMhpyszuOkmS0"
CHAT_ID = "7330431242"

try:
    pytrends = TrendReq(hl='en-US', tz=360)

    trending_en = pytrends.trending_searches(pn='united_states')[0].head(5).tolist()

    message = "🌍 5 English Trends\n\n"

    for i, trend in enumerate(trending_en, 1):
        message += f"{i}- {trend}\n"

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    print("Trends sent")

except Exception as e:
    print(e)
