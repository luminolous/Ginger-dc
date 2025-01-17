import feedparser

rss_url = "https://techcrunch.com/category/artificial-intelligence/feed/"

feed = feedparser.parse(rss_url)

for entry in feed.entries:
    print(f"Title: {entry.title}")
    print(f"Published: {entry.published}")
    print(f'Summary: {entry.summary}')
    print(f"Link: {entry.link}")
    print("-" * 50)

