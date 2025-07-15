from flask import Flask, render_template, request
from sentiment import analyze_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    user_sentence = request.form.get('sentence')
    user_sentiment = ""
    confidence = 0.0

    if user_sentence:
        sentiment, confidence = analyze_sentiment(user_sentence)
        user_sentiment = sentiment

    return render_template(
        'index.html',
        user_sentence=user_sentence,
        user_sentiment=user_sentiment,
        confidence=confidence
    )

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
