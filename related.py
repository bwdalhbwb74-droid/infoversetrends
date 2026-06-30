"""
InfoVerse Hub V2
Related Articles Builder
"""

import json
import os


PUBLISHED_FILE = "published.json"


class RelatedBuilder:

    def __init__(self):

        pass


    def load_articles(self):

        if not os.path.exists(PUBLISHED_FILE):

            return []

        with open(
            PUBLISHED_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    def find_related(
        self,
        article,
        limit=4,
    ):

        articles = self.load_articles()

        related = []

        category = article.get(
            "category",
            ""
        )

        for item in articles:

            if item.get("category") != category:
                continue

            if item.get("title") == article.get("title"):
                continue

            related.append(item)

            if len(related) >= limit:
                break

        return related


related_builder = RelatedBuilder()
    def render(
        self,
        related,
    ):
        """
        Render related articles HTML.
        """

        if not related:
            return ""

        html = []

        for article in related:

            html.append(f"""
<div class="related-card">

<a href="{article.get('url','')}">

<img
src="{article.get('image','')}"
alt="{article.get('title','')}">

<h3>

{article.get('title','')}

</h3>

<p>

{article.get('description','')}

</p>

</a>

</div>
""")

        return "\n".join(html)


    def build(
        self,
        article,
    ):
        """
        Build related articles.
        """

        related = self.find_related(
            article
        )

        return self.render(
            related
        )


related_builder = RelatedBuilder()
