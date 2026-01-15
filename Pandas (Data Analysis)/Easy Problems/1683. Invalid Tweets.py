# Efficient boolean indexing method
tweets = tweets[tweets['content'].str.len() > 15][['tweet_id']]