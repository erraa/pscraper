#!/usr/bin/env python

import feedparser
import settings
import time
import json
import requests

def get_feed(url, last_url):
    """ Get feed

    Takes an rss feed with latest entry and the previous entry

    Args:
        url: rss feed url
        last_url: The previous url
    Returns:
        A dict with pic_url and last_url keys

    """
    f = feedparser.parse(url)
    try:
        pic_url = f.entries[0]['id']
    except:
        return {}
    if pic_url == last_url:
        return {}

    return_dict = {'pic_url': pic_url, 'last_url': pic_url}
    return return_dict

class Message(object):
    def __init__(self, url):
        self.content = url

def post_to_discord(pic_url):
    """{"embeds": [{"url": "https://example.com", "type": "link", "description": "det vet inte du", "title": "Topic Title"}]}"""
    message = Message(pic_url).__dict__
    data = message
    headers = {"Content-Type": "application/json"}
    r = requests.post(settings.webhook, data=json.dumps(data), headers=headers)
    print r.status_code
    if r.status_code == 204:
        print "Posted Url {}".format(pic_url)
    else:
        print "Couldnt post to discord {}".format(r.text)

def main():
    last_url = ''
    url = settings.url
    while True:
        pic_dict = get_feed(url, last_url)
        if not pic_dict:
            time.sleep(5)
            continue
        post_to_discord(pic_dict['pic_url'])
        last_url = pic_dict['last_url']
        time.sleep(5)

if __name__ == "__main__":
    main()
