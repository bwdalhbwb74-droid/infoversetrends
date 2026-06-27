import time
import json
import google.generativeai as genai

from config import GEMINI_API_KEY

# ==========================================
# CONFIGURE GEMINI
# ==========================================

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)
# ==========================================
# BUILD PROMPT
# ==========================================

def build_prompt(topic):

    language = topic.get("language", "ar")

    if language == "ar":

        return f"""
أنت كاتب محتوى SEO محترف.

اكتب مقالًا عربيًا احترافيًا بناءً على المعلومات التالية.

العنوان:
{topic["title"]}

الملخص:
{topic["summary"]}

المصدر:
{topic["source"]}

الرابط:
{topic["link"]}

المطلوب:

- عنوان SEO احترافي.
- Meta Description.
- Slug باللغة الإنجليزية.
- مقال بين 1500 و2500 كلمة.
- مقدمة.
- عناوين H2 و H3.
- خاتمة.
- FAQ.
- لا تنسخ من المصدر.
- اكتب بأسلوب طبيعي وسهل.
- أرجع النتيجة بصيغة JSON فقط.

"""

    return f"""
You are a professional SEO writer.

Write a unique English article based on:

Title:
{topic["title"]}

Summary:
{topic["summary"]}

Source:
{topic["source"]}

Link:
{topic["link"]}

Requirements:

- SEO Title
- Meta Description
- URL Slug
- 1500-2500 words
- H2/H3 headings
- FAQ
- Conclusion
- Do not copy the source.
- Return JSON only.

"""
# ==========================================
# GENERATE ARTICLE
# ==========================================

def generate_article(topic):

    prompt = build_prompt(topic)

    try:

        response = model.generate_content(
            prompt
        )

        text = response.text.strip()

        # إزالة Markdown إذا أضافه Gemini

        text = text.replace(
            "```json",
            ""
        )

        text = text.replace(
            "```",
            ""
        )

        text = text.strip()

        start = text.find("{")
        end = text.rfind("}")

        if start == -1 or end == -1:

            raise Exception(
                "JSON not found."
            )

        json_text = text[start:end + 1]

        article = json.loads(
            json_text
        )

        return article

    except Exception as e:

        print("=" * 50)
        print("Gemini Error")
        print(e)
        print("=" * 50)

        return None
# ==========================================
# PUBLIC FUNCTION
# ==========================================

def create_article(topic):

    for attempt in range(3):

        article = generate_article(topic)

        if article is not None:

            return {
                "success": True,
                "data": article
            }

        print(
            f"Retry {attempt + 1}/3..."
        )

        time.sleep(2)

    return {
        "success": False,
        "error": "Failed to generate article."
    }
