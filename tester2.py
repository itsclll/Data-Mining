#Hindi ko mapagana kasi di ko maayos python version
import snscrape.modules.twitter as sntwitter
import pandas as pd
import re

# Parameters
query = "global warming"
max_tweets = 200  # Number of tweets to fetch
start_date = "2024-01-01"
end_date = "2025-6-23"

# Store tweet data
tweets_data = []

# Scrape tweets
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{query} since:{start_date} until:{end_date}').get_items()):
    if i >= max_tweets:
        break
    tweets_data.append({
        "ID": i + 1,
        "Date": tweet.date.strftime("%Y-%m-%d"),
        "Source": "Twitter",
        "Author": tweet.user.username,
        "Text": tweet.content,
        "Subtopic": "",
        "Sentiment": "",
        "Engagement": tweet.likeCount + tweet.retweetCount + tweet.replyCount
    })

# Create DataFrame
df = pd.DataFrame(tweets_data)

# Basic cleaning (optional)
def clean_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

df["Text"] = df["Text"].apply(clean_text)

# Save to CSV
df.to_csv("global_warming_dataset_snscrape.csv", index=False)
print("Dataset saved as 'global_warming_dataset_snscrape.csv'")
# Preview sample
df.head()
