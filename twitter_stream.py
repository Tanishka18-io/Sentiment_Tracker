import tweepy

# Replace with your Bearer Token from Twitter Developer Portal
bearer_token = "AAAAAAAAAAAAAAAAAAAAANkn3AEAAAAAFe02t1uozwAUxj5nxrEFJpZ29DQ%3D9iXmIYdl65gqdjympWy8YJaCtDyBaCOMvjaTTqhbENMTRrrm9z"

# Create a Tweepy client using Bearer Token
client = tweepy.Client(bearer_token=bearer_token)

# Function to fetch recent tweets
def get_tweets(keyword):
    try:
        # Search recent tweets containing the keyword
        tweets = client.search_recent_tweets(query=keyword, max_results=10)

        # Extract tweet text
        tweet_texts = [tweet.text for tweet in tweets.data] if tweets.data else []
        return tweet_texts

    except Exception as e:
        print(f"Error fetching tweets: {e}")
        return []
# if __name__ == "__main__":
#     tweets = get_tweets("iPhone")
#     for t in tweets:
#         print(t)
def get_tweets(keyword):
    try:
        tweets = client.search_recent_tweets(query=keyword, max_results=10)
        print("Raw response:", tweets)
        tweet_texts = [tweet.text for tweet in tweets.data] if tweets.data else []
        return tweet_texts
    except Exception as e:
        print(f"Error fetching tweets: {e}")
        return []
