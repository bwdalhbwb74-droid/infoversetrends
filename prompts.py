"""
InfoVerse Hub V2
ChatGPT Prompt Generator
"""


def arabic_prompt(topic):

    return f"""
أنت كاتب محتوى عربي محترف وخبير SEO.

ستكتب مقالاً احترافياً جاهزاً للنشر في موقع InfoVerse Hub.

اعتمد فقط على بيانات الموضوع التالية:

========================================

العنوان:
{topic["title"]}

التصنيف:
{topic["category"]}

الملخص:
{topic["summary"]}

========================================

المطلوب:

1. اكتب عنوان SEO احترافياً يجذب النقرات.

2. اكتب Meta Description احترافياً بين 140 و160 حرفاً.

3. اكتب مقالاً احترافياً يتراوح بين 450 و1000 كلمة حسب طبيعة الموضوع.

4. اجعل أسلوب الكتابة بشرياً وطبيعياً.

5. لا تنسخ أي فقرة من الملخص.

6. استخدم الكلمات المفتاحية بشكل طبيعي.

7. إذا كان الموضوع خبراً فاشرح الخبر وتأثيره وأهميته، ولا تكتفِ بإعادة صياغته.

8. إذا كان الموضوع عن هاتف أو سيارة أو منتج تقني فأضف أهم المواصفات والمميزات والعيوب إن توفرت.

9. إذا كانت المقارنة مناسبة فأضف جدول مقارنة.

10. إذا كانت النصائح مناسبة فأضف قسم نصائح.

11. أضف قسم FAQ يحتوي على 5 أسئلة وإجابات.

12. استخدم HTML البسيط فقط.
13. المسموح استخدام الوسوم التالية فقط:

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

14. لا تستخدم Markdown.

15. لا تنشئ صفحة HTML كاملة.

16. لا تضف:

<html>
<head>
<body>
<style>
<script>

17. لا تضع أي صور داخل المقال.

18. لا تكتب أسماء الصور أو أماكنها.

19. لا تنشئ Slug أو Canonical أو Open Graph أو Twitter Cards أو Schema، فهذه مسؤولية البوت.

20. أرجع محتوى المقال فقط بصيغة HTML.

21. الهدف أن يقوم البوت بعد ذلك ببناء الصفحة، وإضافة الصور، وتحسين SEO، وإنشاء المعاينة، ثم نشر المقال.

22. ابدأ مباشرة بكتابة المقال دون أي مقدمة أو شرح خارج المقال.

"""
def english_prompt(topic):

    return f"""
You are a professional SEO content writer.

Write a high-quality article for InfoVerse Hub based ONLY on the information below.

========================================

Title:
{topic["title"]}

Category:
{topic["category"]}

Summary:
{topic["summary"]}

========================================

Requirements:

1. Write in fluent, natural English.

2. Create an attractive SEO title.

3. Write a meta description between 140 and 160 characters.

4. Write between 450 and 1000 words depending on the topic.

5. Make the article completely original.

6. Do NOT copy the summary.

7. Expand the topic professionally.

8. Use the primary keyword naturally.

9. Include related keywords.

10. If this is a news topic, explain why it matters instead of simply rewriting it.

11. If this is about a phone, car, or tech product, include specifications, advantages, disadvantages, and key features when appropriate.

12. Add a comparison table if relevant.
13. Add a Tips section if appropriate.

14. Add an FAQ section with 5 questions and answers.

15. Use ONLY these HTML tags:

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

16. Do NOT use Markdown.

17. Do NOT generate a full HTML page.

18. Do NOT include:

<html>
<head>
<body>
<style>
<script>

19. Do NOT insert images.

20. Do NOT include image filenames or image placeholders.

21. Do NOT generate Slug, Canonical, Open Graph, Twitter Cards, or Schema. Those will be generated automatically by the publishing bot.

22. Return ONLY the article body in clean HTML.

23. The publishing bot will automatically build the final webpage, optimize SEO, generate metadata, fetch images, create the preview, and publish the article.

24. Start writing the article immediately.

"""
