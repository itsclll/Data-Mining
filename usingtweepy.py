#Gumagana to
import tweepy
import pandas as pd

# STEP 1: Insert your actual Bearer Token here
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAEDT2gEAAAAADDjH6jFZcOuqm2AvbEeXlrKb1sY%3DmMdZIB5GMoPnP1TkXy07MsC1dXg38Afqce0QnZc7lnDYtlAcqO'  # Replace with your token

# STEP 2: Authenticate
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# STEP 3: Define your query
query = "global warming -is:retweet lang:en"  # No retweets, only English
max_results = 1000

# STEP 4: Search recent tweets
response = client.search_recent_tweets(
    query=query,
    max_results=max_results,
    tweet_fields=["created_at", "lang", "public_metrics"],
    user_fields=["username"],
    expansions=["author_id"]
)

tweets_data = []
if response.data:
    for i, tweet in enumerate(response.data):
        author = users.get(str(tweet.author_id), "UnknownUser")
        engagement = tweet.public_metrics['like_count'] + tweet.public_metrics['retweet_count'] + tweet.public_metrics['reply_count']

        tweets_data.append({
            "ID": i + 1,
            "Date": tweet.created_at.strftime("%Y-%m-%d"),
            "Source": "Twitter",
            "Author": author,
            "Text": tweet.text,
            "Subtopic": "",      # To be filled manually or via topic modeling
            "Sentiment": "",     # To be filled via sentiment analysis
            "Engagement": engagement
        })
else:
    print("No tweets found.")

# STEP 6: Save as DataFrame and CSV
df = pd.DataFrame(tweets_data)
df.to_csv("tweepy_global_warming_dataset.csv", index=False)
print(" Saved dataset as tweepy_global_warming_dataset1.csv")

# Optional: Preview
df.head()