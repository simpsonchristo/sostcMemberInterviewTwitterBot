#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Twitter Bot for SOSTC Interviews"""
from ConfigTwitterApi import create_api, tweetformatter
#from time import sleep
import requests
from bs4 import BeautifulSoup as bs
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
tweets = []
starterTweet = []

#grab interview
fo = open("interviewUrls","r")
while True:
    try:
        url = fo.readline().rstrip('\n')
        rawHtml = requests.get(url)
        soup = bs(rawHtml.content, 'html.parser')
        interview = soup.find_all("div", {"class": "wp-block-jetpack-layout-grid-column wp-block-jetpack-layout-grid__padding-none"})[-1]
        questions = []
        qs = interview.find_all("h6")
        answers = []
        ans = interview.find_all("p")
        qanda = []
        
        for i in range(0,len(qs)):
            questions.append(qs[i].text)
        for i in range(1):
            starterTweet.append(ans[i].text)
        for i in range(1,len(ans)):
            answers.append(ans[i].text)
        
        
        for i in range(0,len(questions)):
            qanda.append(questions[i])
            qanda.append(answers[i])
        
        tweets.append(tweetformatter(qanda))
    except:
        if(fo.readline()==''):
            fo.close()
            break