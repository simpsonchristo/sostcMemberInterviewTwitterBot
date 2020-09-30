#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Twitter Bot for SOSTC Interviews"""
from ConfigTwitterApi import create_api
import datetime
import tweepy
"""Python 3.6.9
   Simpson Aerospace (c) 2020
   Christopher Simpson: christopher.r.simpson@simpsonaerospace.com"""
#------------------------------------------------------------------------------
#necessary keys
fo = open("../twitterbotkeys", "r")
consumer_key = fo.readline().rstrip('\n')
consumer_secret = fo.readline().rstrip('\n')
access_token = fo.readline().rstrip('\n')
access_token_secret = fo.readline().rstrip('\n')
fo.close()

api = create_api(consumer_key, consumer_secret, access_token, access_token_secret)
today = datetime.date.today()
for tweet in tweepy.Cursor(api.search_users,
                           q='@aiaa').items(10):
    try:
        if(tweet.name=='AIAA'):
            print(tweet.name, tweet.id)
            statuses = api.user_timeline(id=tweet.id,
                                         count=10,
                                         tweet_mode='extended')
            for info in statuses[:3]:
                print(info.full_text)
                
        
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
