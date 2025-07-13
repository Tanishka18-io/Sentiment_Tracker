from flask import Flask, render_template, request
from offline_stream import get_offline_tweets
from twitter_stream import get_tweets
from sentiment import analyze_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    sentiments = []
    keyword = ""
    mode = "live"
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}

    if request.method == 'POST':
        keyword = request.form['keyword']
        mode = request.form.get('mode')

        # Choose live or offline tweets
        if mode == "offline":
            tweets = [t for t in get_offline_tweets() if keyword.lower() in t.lower()]
        else:
            tweets = get_tweets(keyword)

        # Analyze sentiments
        sentiments = [(tweet, analyze_sentiment(tweet)) for tweet in tweets]

        for _, sentiment in sentiments:
            if sentiment in sentiment_counts:
                sentiment_counts[sentiment] += 1

    return render_template(
        'index.html',
        sentiments=sentiments,
        keyword=keyword,
        counts=sentiment_counts,
        mode=mode
    )

# if __name__ == '__main__':
#     app.run(debug=True)


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
