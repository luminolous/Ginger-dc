import time
import feedparser
import schedule

def fetch_news():
    rss_url = "https://techcrunch.com/category/artificial-intelligence/feed/"
    feed = feedparser.parse(rss_url)
    for entry in feed.entries[:5]:
        print(f"Title: {entry.title}")
        print(f"Published: {entry.published}")
        print(f'Summary: {entry.summary}')
        print(f"Link: {entry.link}")
        print("-" * 50)

schedule.every(10).minutes.do(fetch_news)

i = 0
while True:
    print(f"Time: {i + 1}")
    schedule.run_pending()
    time.sleep(1)
    i += 1
