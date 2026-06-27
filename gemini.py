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

        # إزالة ```json إذا أضافها Gemini

        if text.startswith("```json"):
            text = text[7:]

        if text.startswith("```"):
            text = text[3:]

        if text.endswith("```"):
            text = text[:-3]

        text = text.strip()

        return json.loads(text)

    except Exception as e:

        print("Gemini Error")
        print(e)

        return None
# ==========================================
# PUBLIC FUNCTION
# ==========================================

def create_article(topic):

    article = generate_article(topic)

    if article is None:

        return {
            "success": False,
            "error": "Gemini failed."
        }

    return {
        "success": True,
        "data": article
    }
    
