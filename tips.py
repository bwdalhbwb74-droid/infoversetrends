"""
InfoVerse Hub V2
Buying Tips Builder
"""


class TipsBuilder:

    def __init__(self):

        self.categories = [
            "phone",
            "iphone",
            "android",
            "laptop",
            "car",
            "camera",
            "tablet",
            "watch",
            "headphone",
            "هاتف",
            "جوال",
            "آيفون",
            "ايفون",
            "سيارة",
            "سيارات",
            "لابتوب",
            "كاميرا",
            "سماعات",
            "ساعة",
        ]


    def needs_tips(
        self,
        article,
    ):
        """
        Check if article needs buying tips.
        """

        title = article.get(
            "title",
            ""
        ).lower()

        for keyword in self.categories:

            if keyword.lower() in title:

                return True

        return False


    def build(
        self,
        article,
    ):
        """
        Build buying tips section.
        """

        if not self.needs_tips(article):

            return ""

        return """
<section class="buying-tips">

<h2>

نصائح قبل الشراء

</h2>

<ul>

<li>حدد ميزانيتك قبل اتخاذ القرار.</li>

<li>قارن المواصفات والسعر.</li>

<li>تأكد من توفر الضمان.</li>

<li>راجع تقييمات المستخدمين.</li>

<li>اختر المنتج المناسب لاحتياجاتك.</li>

</ul>

</section>
"""


tips_builder = TipsBuilder()
