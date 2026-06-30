"""
InfoVerse Hub V2
FAQ Builder
"""

from bs4 import BeautifulSoup


class FAQBuilder:

    def __init__(self):

        pass


    def extract(self, html):
        """
        Extract FAQ from article.
        """

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        faq = []

        questions = soup.find_all("h3")

        for question in questions:

            answer = question.find_next("p")

            if not answer:
                continue

            faq.append({
                "question": question.get_text(strip=True),
                "answer": answer.get_text(" ", strip=True),
            })

        return faq


    def render(self, faq):

        if not faq:

            return ""

        html = [
            '<section class="faq">',
            '<h2>الأسئلة الشائعة</h2>'
        ]

        for item in faq:

            html.append(f"""
<div class="faq-item">

<div class="faq-question">

{item["question"]}

</div>

<div class="faq-answer">

{item["answer"]}

</div>

</div>
""")

        html.append("</section>")

        return "\n".join(html)


    def build(self, article_html):

        faq = self.extract(
            article_html
        )

        return self.render(
            faq
        )


faq_builder = FAQBuilder()
