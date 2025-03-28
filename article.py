from dataclasses import dataclass


@dataclass
class Article:
    title: str
    content: str
    image: str | None = None


class Database:
    articles = []

    @staticmethod
    def save(article: Article):
        if Database.find_article_by_title(article.title) is not None:
            return False

        Database.articles.append(article)
        return True

    @staticmethod
    def get_all_articles():
        return Database.articles
    
    @staticmethod
    def find_article_by_title(title: str):
        for article in Database.articles:
            if article.title == title:
                return article
        return None


database = {
    "spacex": {
        "article_title": "SpaceX Crew-10",
        "article_text": """
SpaceX Crew-10 — планируемый десятый пилотируемый полёт американского космического корабля
Crew Dragon компании SpaceX в рамках программы NASA Commercial Crew Program.
Корабль доставит четырёх членов экипажа миссии Crew-10 и космических экспедиций МКС-72/73 на Международную космическую станцию (МКС).
Запуск планируется провести 12 марта 2025 года.
""",
        "article_image": "SpaceX_Crew_Dragon.jpg"
    },

    "cosmos": {
        "article_title": "Космос (философия)",
        "article_text": """
Ко́смос (др.-греч. κόσμος «порядок, гармония») — понятие древнегреческой философии и культуры,
представление о природном мире как о пластически упорядоченном гармоническом целом.
Противопоставлялся хаосу.
Греки соединяли в понятии «космос» две функции — упорядочивающую и эстетическую.
""",
        "article_image": "Cosmos.png"
    }
}
