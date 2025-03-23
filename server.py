from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("ruwiki.html")

database = {
    "sonic": {
        "title_article": "Ёж Соник",
        "text_article": """
Соник — синий антропоморфный ёж, созданный художником Наото Осимой, программистом Юдзи Накой и дизайнером Хирокадзу Ясухарой. Во время разработки было предложено множество образов главного героя будущей игры, но разработчики остановились на ёжике синего цвета. Своё имя Соник получил за способность бегать на сверхзвуковых скоростях (англ. sonic — «звуковой; со скоростью звука»). Геймплей за Соника в большинстве игр серии Sonic the Hedgehog заключается в быстром прохождении уровней и битвах с врагами, для атаки которых Соник сворачивается в шар во время прыжка. Немаловажную роль для Соника играют золотые кольца, служащие ему в качестве защиты. Главным антагонистом героя является доктор Эггман, который хочет захватить мир и построить свою империю «Эггманленд».
""",
        "article_image_title": "Соник",
        "article_image_path": "sonic.png"
    },
    "naklz": {
        
    }
}

# /article/sonic
# /article/cosmos
# /article/12321421
@app.route("/article/<name>")
def article(name):
    article = database[name]
    return render_template(
        'article.html', 
        title_article=article["title_article"],
        text_article=article["text_article"],
        article_image_title=article["article_image_title"],
        article_image_path=article["article_image_path"])


@app.route("/add_article", methods=["GET", "POST"])
def add_article():
    # Если по маршруту /add_article пришел GET-запрос,
    # то необходимо вернуть HTML-страничку и созданием статье
    if request.method == "GET":
        return render_template("add_article.html")
    
    # Тут обработка POST-запроса...
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
    