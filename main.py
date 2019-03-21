import requests
import tweepy
import time
import os


CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

site = "https://petition.parliament.uk/petitions/241584.json"

def get_json(url):
    try:
        return requests.get(url)
    except requests.exceptions.HTTPError as e:
        print('whoops try again')
        print(e)
        exit(1)

def get_top_countries():

    json = get_json(site).json()
    total_signatures = json['data']['attributes']['signature_count']
    count_by_country = (json['data']['attributes']['signatures_by_country'])
    # sort by votes
    country_counts = sorted(count_by_country, key=lambda i: i['signature_count'])
    # select top 10
    top10_countries = country_counts[-9:]
    # reverse list of top 10
    top10 = sorted(top10_countries, key=lambda i: i['signature_count'], reverse=True)

    top_tweet = "Top 10 countries by vote - https://petition.parliament.uk/petitions/241584 \n \n"
    top_tweet += 'Total signatures: {} \n \n'.format(total_signatures)

    for country in top10:
        top_tweet += ('{}: {}\n').format(country["name"], country["signature_count"])
    top_tweet += '#RevokeA50Now #RevokeArt50'
    return top_tweet

def tweet_top_10_countries(event, context):
    try:
        return api.update_status(get_top_countries())
    except tweepy.TweepError as e:
        print(e)
        exit(1)

def get_top_constituency():
    json = get_json(site).json()
    totals_by_constit = json['data']['attributes']['signatures_by_constituency']
    sorted_totals_by_constit = sorted(totals_by_constit, key=lambda i: i['signature_count'])
    top10_constit = sorted_totals_by_constit[-5:]
    sorted_top10 = sorted(top10_constit, key=lambda i: i['signature_count'], reverse=True)
    top10_constit_tweet = "Top votes by constituency - https://petition.parliament.uk/petitions/241584 \n \n"

    for constit in sorted_top10:
        top10_constit_tweet += '{}: {}\n'.format(constit['name'], constit['signature_count'])
    top10_constit_tweet += '#RevokeA50Now #RevokeArt50'
    return top10_constit_tweet

def tweet_top_consituency(event, context):
    try:
        return api.update_status(get_top_constituency())
    except tweepy.TweepError as e:
        print(e)
        exit(1)
