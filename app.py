from flask import Flask, render_template, request
from scraper import get_reviews
from sentiment import analyze_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiments = {"Positive": 0, "Negative": 0, "Neutral": 0}
    reviews = []

    if request.method == 'POST':
        product_url = request.form['url']
        reviews = get_reviews(product_url, max_reviews=30)
        for r in reviews:
            sentiment = analyze_sentiment(r)
            sentiments[sentiment] += 1

    return render_template('index.html', sentiments=sentiments, reviews=reviews)

if __name__ == '__main__':
    app.run(debug=True)
