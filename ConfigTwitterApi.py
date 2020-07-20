#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Twitter Bot Login"""
import tweepy
import os
import logging
"""Python 3.6.9
   Simpson Aerospace (c) 2020
   Christopher Simpson: christopher.r.simpson@simpsonaerospace.com"""
#------------------------------------------------------------------------------
logger = logging.getLogger()

def create_api():
    #grab the keys
    consumer_key        = os.getenv("CONSUMER_KEY")
    consumer_secret     = os.getenv("CONSUMER_SECRET")
    access_token        = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")   
    
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