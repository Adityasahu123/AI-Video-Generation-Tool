import feedparser
from newspaper import Article

# Reliable BBC Technology RSS
rss_url = "http://feeds.bbci.co.uk/news/technology/rss.xml"

feed = feedparser.parse(rss_url)

entry = feed.entries[0]   # top trending news
title = entry.title
link = entry.link

print("TITLE:")
print(title)
print("\nLINK:")
print(link)

# Extract FULL article text from the website
article = Article(link)
article.download()
article.parse()

text = article.text.strip()

print("\nARTICLE PREVIEW:")
print(text[:500])

with open("news_title.txt", "w", encoding="utf-8") as f:
    f.write(title)

with open("news_text.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("\n✅ Saved news_title.txt and news_text.txt")
print("✅ news_text length:", len(text))
