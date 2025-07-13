def get_offline_tweets(keyword):
    try:
        with open("sample_tweets.txt", "r", encoding="utf-8") as f:
            tweets = [line.strip() for line in f if keyword.lower() in line.lower()]
        return tweets
    except Exception as e:
        print("Error loading offline tweets:", e)
        return []
