from flask import Flask, render_template, request
from sentiment import analyze_sentiment
from offline_stream import get_offline_tweets  # or your actual tweet fetcher

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    keyword = request.form.get('keyword')
    user_sentence = request.form.get('sentence')
    sentiments = []
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    user_sentiment = ""

    if keyword:
        tweets = [t for t in get_offline_tweets() if keyword.lower() in t.lower()]
        for tweet in tweets:
            sentiment, confidence = analyze_sentiment(tweet)
            sentiments.append((tweet, sentiment, confidence))
            sentiment_counts[sentiment] += 1

    if user_sentence:
        sentiment, confidence = analyze_sentiment(user_sentence)
        user_sentiment = f"{sentiment} ({confidence})"

    return render_template(
        'index.html',
        keyword=keyword,
        sentiments=sentiments,
        counts=sentiment_counts,
        user_sentence=user_sentence,
        user_sentiment=user_sentiment
    )

# ✅ THIS SHOULD BE OUTSIDE THE FUNCTION!
if __name__ == '__main__':
    app.run(debug=True)
