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

    # ✍️ For direct sentence prediction
    user_sentence = ""
    user_sentiment = ""

    if request.method == 'POST':
        # Get keyword from tweet search form
        keyword = request.form.get('keyword', "")
        if keyword:
            tweets = get_offline_tweets(keyword)
            sentiments = [(tweet, analyze_sentiment(tweet)) for tweet in tweets]
            for _, sentiment in sentiments:
                if sentiment in sentiment_counts:
                    sentiment_counts[sentiment] += 1

        # Get custom sentence from user
        user_sentence = request.form.get('sentence', "")
        if user_sentence:
            user_sentiment = analyze_sentiment(user_sentence)

    return render_template(
        'index.html',
        sentiments=sentiments,
        keyword=keyword,
        counts=sentiment_counts,
        user_sentence=user_sentence,
        user_sentiment=user_sentiment
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
