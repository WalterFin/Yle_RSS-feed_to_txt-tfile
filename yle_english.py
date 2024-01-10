import feedparser
import time
#RSS feed url
feed = feedparser.parse("https://feeds.yle.fi/uutiset/v1/recent.rss?publisherIds=YLE_NEWS")

#create file name with the currrent day and time
timestr = time.strftime("%Y%m%d-%H%M%S")
#write rss responses to txt file
with open(timestr+".txt", "w") as file:
    for entry in feed.entries:

        article_title = entry.title
        article_link = entry.link
        article_published_at = entry.published

        print ("{}".format(article_title))
        print ("[{}]".format(article_link))
        print ("Published at {}".format(article_published_at))
        file.write("{}\n".format(article_title))
        file.write("{}\n".format(article_link))
        file.write("Published at: {}\n".format(article_published_at))
        file.write("\n")

file.close()
print("RSS feed saved to txt file.")