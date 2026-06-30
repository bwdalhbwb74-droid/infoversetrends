"""
InfoVerse Hub V2
Advanced Image Engine

Priority:

1. Pexels
2. Pixabay
3. Openverse
4. Wikimedia Commons
5. Lorem Picsum

The engine automatically:

- Searches images
- Downloads images
- Converts to WebP
- Compresses images
- Creates SEO filenames
- Generates ALT text
- Avoids duplicate images
- Returns featured image
- Returns article images
"""

import os
import re
import requests
from io import BytesIO

from PIL import Image

from config import (
    PEXELS_API_KEY,
    PIXABAY_API_KEY,
)

IMAGE_FOLDER = "images"

PEXELS_URL = "https://api.pexels.com/v1/search"

PIXABAY_URL = "https://pixabay.com/api/"

OPENVERSE_URL = "https://api.openverse.org/v1/images/"

WIKIMEDIA_URL = "https://commons.wikimedia.org/w/api.php"

LOREM_PICSUM = "https://picsum.photos/1200/800"


class ImageEngine:

    def __init__(self):

        self.used_urls = set()

        self.used_keywords = set()

        os.makedirs(
            IMAGE_FOLDER,
            exist_ok=True,
        )
            def clean_keyword(self, text):
        """
        Clean keyword for searching.
        """

        text = text.lower()

        text = re.sub(r"<.*?>", "", text)

        text = re.sub(r"[^\w\s-]", "", text)

        text = re.sub(r"\s+", " ", text)

        return text.strip()


    def seo_filename(self, keyword, index=1):
        """
        Generate SEO-friendly filename.
        """

        keyword = self.clean_keyword(keyword)

        keyword = keyword.replace(" ", "-")

        return f"{keyword}-{index}.webp"


    def create_alt_text(self, keyword):
        """
        Generate image ALT text.
        """

        keyword = keyword.strip()

        return f"{keyword} illustration"


    def extract_keywords(self, article):

        """
        Extract search keywords from article.
        """

        keywords = []

        title = article.get("title", "")

        if title:
            keywords.append(title)

        for heading in article.get("headings_h2", []):

            heading = heading.strip()

            if len(heading) > 5:
                keywords.append(heading)

        unique = []

        for keyword in keywords:

            keyword = self.clean_keyword(keyword)

            if not keyword:
                continue

            if keyword in self.used_keywords:
                continue

            self.used_keywords.add(keyword)

            unique.append(keyword)

        return unique
            def search_pexels(self, keyword):
        """
        Search image from Pexels.
        """

        if not PEXELS_API_KEY:
            return None

        headers = {
            "Authorization": PEXELS_API_KEY
        }

        params = {
            "query": keyword,
            "per_page": 10,
            "orientation": "landscape"
        }

        try:

            response = requests.get(
                PEXELS_URL,
                headers=headers,
                params=params,
                timeout=30
            )

            if response.status_code != 200:
                return None

            data = response.json()

            photos = data.get("photos", [])

            if not photos:
                return None

            for photo in photos:

                image_url = photo["src"]["large2x"]

                if image_url in self.used_urls:
                    continue

                self.used_urls.add(image_url)

                return {
                    "provider": "Pexels",
                    "url": image_url,
                    "author": photo.get("photographer", ""),
                    "page": photo.get("url", ""),
                    "alt": photo.get("alt", keyword),
                }

        except Exception as error:

            print(f"Pexels Error: {error}")

        return None
            def search_pixabay(self, keyword):
        """
        Search image from Pixabay.
        """

        if not PIXABAY_API_KEY:
            return None

        params = {
            "key": PIXABAY_API_KEY,
            "q": keyword,
            "image_type": "photo",
            "orientation": "horizontal",
            "safesearch": "true",
            "per_page": 10,
        }

        try:

            response = requests.get(
                PIXABAY_URL,
                params=params,
                timeout=30,
            )

            if response.status_code != 200:
                return None

            data = response.json()

            hits = data.get("hits", [])

            if not hits:
                return None

            for image in hits:

                image_url = image.get("largeImageURL")

                if not image_url:
                    continue

                if image_url in self.used_urls:
                    continue

                self.used_urls.add(image_url)

                return {
                    "provider": "Pixabay",
                    "url": image_url,
                    "author": image.get("user", ""),
                    "page": image.get("pageURL", ""),
                    "alt": image.get("tags", keyword),
                }

        except Exception as error:

            print(f"Pixabay Error: {error}")

        return None


    def search_image(self, keyword):
        """
        Search image using providers by priority.
        """

        image = self.search_pexels(keyword)

        if image:
            return image

        image = self.search_pixabay(keyword)

        if image:
            return image

        return None
            def search_openverse(self, keyword):
        """
        Search image from Openverse.
        """

        params = {
            "q": keyword,
            "page_size": 10,
        }

        try:

            response = requests.get(
                OPENVERSE_URL,
                params=params,
                timeout=30,
            )

            if response.status_code != 200:
                return None

            data = response.json()

            results = data.get("results", [])

            if not results:
                return None

            for image in results:

                image_url = image.get("url")

                if not image_url:
                    continue

                if image_url in self.used_urls:
                    continue

                self.used_urls.add(image_url)

                return {
                    "provider": "Openverse",
                    "url": image_url,
                    "author": image.get("creator", ""),
                    "page": image.get("foreign_landing_url", ""),
                    "alt": image.get("title", keyword),
                }

        except Exception as error:

            print(f"Openverse Error: {error}")

        return None


    def search_wikimedia(self, keyword):
        """
        Search image from Wikimedia Commons.
        """

        params = {
            "action": "query",
            "generator": "search",
            "gsrsearch": keyword,
            "gsrnamespace": 6,
            "prop": "imageinfo",
            "iiprop": "url",
            "format": "json",
        }

        try:

            response = requests.get(
                WIKIMEDIA_URL,
                params=params,
                timeout=30,
            )

            if response.status_code != 200:
                return None

            data = response.json()

            pages = data.get("query", {}).get("pages", {})

            for page in pages.values():

                info = page.get("imageinfo", [])

                if not info:
                    continue

                image_url = info[0].get("url")

                if not image_url:
                    continue

                if image_url in self.used_urls:
                    continue

                self.used_urls.add(image_url)

                return {
                    "provider": "Wikimedia",
                    "url": image_url,
                    "author": "",
                    "page": image_url,
                    "alt": page.get("title", keyword),
                }

        except Exception as error:

            print(f"Wikimedia Error: {error}")

        return None


    def search_image(self, keyword):
        """
        Search image using all providers.
        """

        providers = [
            self.search_pexels,
            self.search_pixabay,
            self.search_openverse,
            self.search_wikimedia,
        ]

        for provider in providers:

            image = provider(keyword)

            if image:
                return image

        return None
            def download_image(self, image, filename):
        """
        Download image and convert to WebP.
        """

        try:

            response = requests.get(
                image["url"],
                timeout=30,
            )

            if response.status_code != 200:
                return None

            img = Image.open(
                BytesIO(response.content)
            ).convert("RGB")

            path = os.path.join(
                IMAGE_FOLDER,
                filename,
            )

            img.save(
                path,
                "WEBP",
                quality=85,
                optimize=True,
            )

            return path

        except Exception as error:

            print(f"Download Error: {error}")

            return None


    def get_featured_image(self, keyword):
        """
        Download featured image.
        """

        image = self.search_image(keyword)

        if not image:
            return None

        filename = self.seo_filename(
            keyword,
            1,
        )

        path = self.download_image(
            image,
            filename,
        )

        if not path:
            return None

        image["path"] = path

        image["alt"] = self.create_alt_text(keyword)

        return image


    def get_article_images(self, keywords):
        """
        Download article images.
        """

        images = []

        index = 2

        for keyword in keywords:

            image = self.search_image(keyword)

            if not image:
                continue

            filename = self.seo_filename(
                keyword,
                index,
            )

            path = self.download_image(
                image,
                filename,
            )

            if not path:
                continue

            image["path"] = path

            image["alt"] = self.create_alt_text(keyword)

            images.append(image)

            index += 1

        return images
            def build_image_package(self, article):
        """
        Build all article images.
        """

        keywords = self.extract_keywords(article)

        if not keywords:
            return {
                "featured": None,
                "images": []
            }

        featured = self.get_featured_image(
            keywords[0]
        )

        article_images = self.get_article_images(
            keywords[1:]
        )

        return {
            "featured": featured,
            "images": article_images
        }


    def distribute_images(self, html, images):
        """
        Insert images before H2 headings.
        """

        if not images:
            return html

        h2_count = html.count("<h2")

        if h2_count == 0:
            return html

        output = html

        index = 0

        while "<h2" in output and index < len(images):

            image = images[index]

            block = f"""
<figure class="article-image">
    <img src="{image['path']}" alt="{image['alt']}" loading="lazy">
</figure>

"""

            output = output.replace(
                "<h2",
                block + "<h2",
                1
            )

            index += 1

        return output
                def get_images(self, article):
        """
        Main image engine.
        """

        package = self.build_image_package(article)

        return package


image_engine = ImageEngine()
