from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Create analyzer object
analyzer = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    score = analyzer.polarity_scores(text)

    if score['compound'] >= 0.05:
        return "Positive"
    elif score['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"
# if __name__ == "__main__":
#     example = "I love this phone, it's amazing!"
#     result = analyze_sentiment(example)
#     print(f"Sentiment: {result}")
