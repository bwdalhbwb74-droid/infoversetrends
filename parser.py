"""
InfoVerse Hub V2
Article Parser
"""

from bs4 import BeautifulSoup


def parse_article(html):
    """
    Parse HTML article.
    """

    soup = BeautifulSoup(html, "html.parser")

    data = {
        "title": "",
        "meta_description": "",
        "headings_h2": [],
        "headings_h3": [],
        "paragraphs": [],
        "lists": [],
        "tables": [],
        "faq": [],
    }

    # H2
    for tag in soup.find_all("h2"):
        data["headings_h2"].append(tag.get_text(strip=True))

    # H3
    for tag in soup.find_all("h3"):
        data["headings_h3"].append(tag.get_text(strip=True))

    # Paragraphs
    for tag in soup.find_all("p"):
        text = tag.get_text(" ", strip=True)

        if text:
            data["paragraphs"].append(text)

    # Lists
    for tag in soup.find_all("ul"):
        items = []

        for li in tag.find_all("li"):
            items.append(li.get_text(" ", strip=True))

        if items:
            data["lists"].append(items)

    # Tables
    for table in soup.find_all("table"):
        data["tables"].append(str(table))

    # First H2 becomes title temporarily
    if data["headings_h2"]:
        data["title"] = data["headings_h2"][0]

    return data
