"""
InfoVerse Hub V2
ChatGPT Prompt Generator
"""


def arabic_prompt(topic):

    return f"""
أنت كاتب محتوى عربي محترف وخبير SEO.

ستكتب مقالاً احترافياً جاهزاً للنشر في موقع InfoVerse Hub.

اعتمد فقط على بيانات الخبر التالية:

========================================

العنوان:
{topic["title"]}

التصنيف:
{topic["category"]}

الملخص:
{topic["summary"]}

المصدر:
{topic["link"]}

========================================

المطلوب:
1. اكتب عنوان SEO احترافي يجذب النقرات.

2. اكتب Meta Description احترافياً بين 140 و160 حرفاً.

3. اكتب مقالاً احترافياً يتراوح بين 450 و1000 كلمة حسب طبيعة الموضوع. لا تُطِل بلا داعٍ، ولا تُقصِّر إذا كان الموضوع يحتاج شرحًا. اجعل طول المقال مناسبًا لتحقيق أفضل تجربة قراءة وأفضل أداء في محركات البحث.

4. اجعل أسلوب الكتابة طبيعياً وكأن كاتباً بشرياً كتبه.

5. لا تنسخ أي فقرة من المصدر.

6. لا تذكر المصدر داخل المقال.

7. استخدم الكلمات المفتاحية بشكل طبيعي.

8. استخدم العناوين التالية عند الحاجة:

<h2>
<h3>
<p>
<ul>
<li>
<table>
<blockquote>

9. لا تستخدم Markdown.

10. لا تنشئ صفحة HTML كاملة.

11. لا تضف:

<html>
<head>
<body>
CSS
JavaScript

12. أرجع محتوى المقال فقط.

13. أضف جدول مقارنة إذا كان مناسباً.

14. أضف قسم مميزات وعيوب إذا كان مناسباً.

15. أضف قسم نصائح أو خطوات إذا كان مناسباً.

16. أضف FAQ يحتوي على 5 أسئلة وإجابات.

17. لا تخترع معلومات غير مؤكدة.

18. إذا لم تكفِ المعلومات الموجودة في الخبر، فاعتمد على معلوماتك العامة الموثوقة لإكمال المقال مع الحفاظ على الدقة.

19. اكتب المقال بأسلوب يناسب النشر في موقع تقني احترافي.

20. ابدأ مباشرة بكتابة المقال.
21. هيكل المقال يجب أن يكون بهذا الترتيب:

- عنوان المقال.
- Meta Description.
- مقدمة.
- جدول المحتويات.
- محتوى المقال.
- خاتمة.
- FAQ.

22. استخدم HTML البسيط فقط.

المسموح:

<h2>
<h3>
<p>
<ul>
<li>
<table>
<tr>
<th>
<td>
<blockquote>

23. ممنوع استخدام:

<html>
<head>
<body>
<style>
<script>
Markdown
24. لا تضع أي صور داخل المقال.

25. لا تكتب أسماء ملفات الصور أو أماكن الصور.

26. لا تكتب Slug.

27. لا تكتب Canonical.

28. لا تكتب Open Graph.

29. لا تكتب Twitter Cards.

30. لا تكتب Schema.

31. لا تبنِ صفحة HTML كاملة، اكتب محتوى المقال فقط.

32. الهدف أن يستلم البوت المقال ويقوم هو ببناء الصفحة وإضافة الصور والـ SEO والمعاينة والنشر.

اكتب المقال الآن مباشرة.

"""
    
    
def english_prompt(topic):

    return f"""
You are a professional SEO writer.

Write a HIGH-QUALITY article based on the following topic.

Topic:
{topic["title"]}

Category:
{topic["category"]}

Source Summary:
{topic["summary"]}

Source URL:
{topic["link"]}

==================================================

Requirements:

1. Write in English.

2. The article must be completely original.

3. Do NOT copy the source.

4. Expand the topic professionally.

5. Article length:
Between 450 and 1000 words.

6. Use SEO best practices.

7. Create an attractive SEO title.

8. Write a meta description (140–160 characters).

9. Use the focus keyword naturally.

10. Include related keywords.

11. Use H2 and H3 headings.

12. Use short paragraphs.

13. Use bullet lists where appropriate.

14. Include one comparison table if useful.

15. Include one FAQ section with at least 3 questions.

16. End with a conclusion.

17. Write naturally for humans.

18. Do not repeat information.

19. Avoid keyword stuffing.

20. Use professional but simple language.

21. Return ONLY the article.

22. Use ONLY simple HTML tags.

Allowed tags:

<h2>
<h3>
<p>
<ul>
<li>
<table>
<tr>
<th>
<td>
<blockquote>

23. Do NOT use:

<html>
<head>
<body>
<style>
<script>
Markdown

24. Do NOT insert images.

25. Do NOT include image filenames.

26. Do NOT generate Slug.

27. Do NOT generate Canonical.

28. Do NOT generate Open Graph.

29. Do NOT generate Twitter Cards.

30. Do NOT generate Schema.

31. Return ONLY the article body in HTML.

32. The publishing bot will build the complete page, generate metadata, add images, create TOC, Schema, Open Graph, and publish automatically.

Start writing the article now.
"""
