#!/usr/bin/env python

import feedparser
import settings
import time

def post_to_discord(url):

def main():
    last_url = ''
    while True:
        url = 'https://{}:{}@pr0nbot.phetast.nu/cgi/rss.cgi?n=1'.format(
                settings.username,
                settings.password
                )
        f = feedparser.parse(url)
        pic_url = f.entries[0]['id']
        if pic_url == posted_url:
            time.sleep(5)
            continue
        else:
            post_to_discord(pic_url)
            last_url = pic_url


if __name__ == "__main__":
    main()
