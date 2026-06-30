"""
InfoVerse Hub V2
Topics Ranking
"""


GOOD_KEYWORDS = [
    "ai",
    "artificial intelligence",
    "openai",
    "chatgpt",
    "google",
    "apple",
    "microsoft",
    "tesla",
    "meta",
    "amazon",
    "nvidia",
    "android",
    "iphone",
    "ios",
    "windows",
    "ذكاء",
    "الذكاء",
    "جوجل",
    "آبل",
    "ابل",
    "مايكروسوفت",
    "تحديث",
    "جديد",
    "إطلاق",
    "رسمي",
]


def calculate_score(article):
    """
    Calculate article score.
    """

    score = 0

    title = article.get("title", "").lower()
    summary = article.get("summary", "").lower()

    # Keyword score
    for keyword in GOOD_KEYWORDS:

        if keyword in title:
            score += 10

        if keyword in summary:
            score += 5

    # Title length
    title_length = len(title)

    if 40 <= title_length <= 100:
        score += 10

    elif 20 <= title_length < 40:
        score += 5

    # Summary exists
    if summary:
        score += 5

    return score


def rank_articles(articles):
    """
    Rank all articles.
    """

    for article in articles:

        article["score"] = calculate_score(article)

    articles.sort(
        key=lambda article: article["score"],
        reverse=True
    )

    return articles


def get_top_articles(articles, limit=10):
    """
    Return top articles.
    """

    ranked = rank_articles(articles)

    return ranked[:limit]
