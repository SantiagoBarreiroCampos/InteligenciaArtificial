# -*- coding: utf-8 -*-

import tweepy
import pandas as pd

consumer_key = "KF6nIjrYBNo4ghRQQSrYuKap8"
consumer_secret = "egLoHiFVOe1RXK3Y27r7zpsIOGOiWLw98qfCtPh2uhkuaHtIgE"
access_token = "1448336514455330827-bo05K7o4t7VMze7Wzi66iBqae7LbIg"
access_secret = "xWLQ9XbfvSCZkTkqOe5gWUJ1pCOHluUUbkrXF83yGutqR"

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
items=10
i=0
array = [""]*10
for tweet in tweepy.Cursor(api.search_tweets, q='covid').items(items):
    array[i] = tweet.text
    i+=1
print(array)

df = pd.DataFrame(array)
print(df)

df.to_excel('resultados.xlsx')