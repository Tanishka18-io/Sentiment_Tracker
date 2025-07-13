from flask import Flask, render_template, request
from offline_stream import get_offline_tweets
from sentiment import analyze_sentiment
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    sentiments = []
    keyword = ""
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}

    if request.method == 'POST':
        keyword = request.form['keyword']
        # ✅ FIX: Pass keyword to the function
        tweets = get_offline_tweets(keyword)
        sentiments = [(tweet, analyze_sentiment(tweet)) for tweet in tweets]

        # Count sentiment types
        for _, sentiment in sentiments:
            if sentiment in sentiment_counts:
                sentiment_counts[sentiment] += 1

    return render_template(
        'index.html',
        sentiments=sentiments,
        keyword=keyword,
        counts=sentiment_counts
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
