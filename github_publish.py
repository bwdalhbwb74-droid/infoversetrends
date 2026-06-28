from github import upload_file


def publish_article(article):

    slug = article["slug"]

    article_html = article["article"]

    html = f"""<!DOCTYPE html>
<html lang="ar">
<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1">

<title>{article["title"]}</title>

<meta name="description" content="{article["meta_description"]}">

</head>

<body>

<h1>{article["title"]}</h1>

{article_html}

</body>
</html>
"""

    path = f"articles/{slug}.html"

    success = upload_file(
        path=path,
        content=html,
        message=f"Publish article: {article['title']}"
    )

    return success
