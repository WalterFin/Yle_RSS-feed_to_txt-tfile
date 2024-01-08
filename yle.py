import feedparser
import time
#RSS-syöte
feed = feedparser.parse("https://feeds.yle.fi/uutiset/v1/majorHeadlines/YLE_UUTISET.rss")

#tiedoston nimi ajalla
timestr = time.strftime("%Y%m%d-%H%M%S")
#kirjoitetaan txt tiedostoon rss-syötteen vastaukset
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
        file.write("Aika: {}\n".format(article_published_at))
        file.write("\n")

file.close()
print("Syötteet tallennettu tiedostoon.")