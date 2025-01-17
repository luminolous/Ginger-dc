import time
import feedparser
import schedule
from add_articles import *

def news_post():
    rss_url = "https://techcrunch.com/category/artificial-intelligence/feed/"
    feed = feedparser.parse(rss_url)
    for entry in feed.entries[:5]:
        if add_article_news:
            return f"Title: {entry.title}\nPublished: {entry.published}\nSummary: {entry.summary}\nLink: {entry.link}"
        else:
            print("There is no new articles available.")

# def news_run():
#     schedule.every(10).minutes.do(fetch_news)

#     i = 0
#     while True:
#         print(f"Time: {i + 1}")
#         schedule.run_pending()
#         time.sleep(1)
#         i += 1
