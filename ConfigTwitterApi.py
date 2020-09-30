#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Twitter Bot Login"""
import tweepy
#import os
import logging
"""Python 3.6.9
   Simpson Aerospace (c) 2020
   Christopher Simpson: christopher.r.simpson@simpsonaerospace.com"""
#------------------------------------------------------------------------------
logger = logging.getLogger()

def create_api(consumer_key, consumer_secret, access_token, access_token_secret):
    #grab the keys
#    consumer_key        = os.getenv("CONSUMER_KEY")
#    consumer_secret     = os.getenv("CONSUMER_SECRET")
#    access_token        = os.getenv("ACCESS_TOKEN")
#    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")   
    
    #Twitter authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    #create API object
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    #test keys
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API Created")
    return api


def tweetAnInterview(text, api):
    TWEET_MAX_LENGTH = 280 - (len("...")+len("[1/1]"))
    to_tweet = []
    startNum = 0
    endNum = 0
    
    for tweet in text:
        counter = 1
        startNum = endNum
        while len(tweet)>TWEET_MAX_LENGTH:
            #grab first 280 characters
            cut = tweet[:TWEET_MAX_LENGTH]
            cut = f"[{counter}/]" + cut[0:] + "..."
            counter+=1
            #save first tweet <= 280
            to_tweet.append(cut)
            
            #replace tweet variable with rest of tweet to keep cutting
            tweet = tweet[TWEET_MAX_LENGTH:]
        counter+=1
        tweet = f"[{counter}/]" + tweet[0:]
        to_tweet.append(tweet)
        endNum = len(to_tweet)
        for message in range(startNum,endNum):
            index = to_tweet[message].find('[')
            index +=3
            to_tweet[message] = to_tweet[message][:index] + f"{counter}" + to_tweet[message][index:]
            
    return to_tweet