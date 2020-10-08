from nytimesarticle import articleAPI
from bs4 import BeautifulSoup
import csv
import requests
import time
import pprint

# input your own NYTimes API keys
api = articleAPI("api_key")

# article count
counter = 0

def getArticle(page, keyword, filename):
    articles = api.search(q=keyword,
                          begin_date=20190301,
                          page=page)

    session = requests.Session()

    for each_a in articles['response']['docs']:
        global counter
        url = each_a['web_url']
        req = session.get(url)
        soup = BeautifulSoup(req.text, "html.parser")

        paragraphs = soup.find_all('p', class_=["css-1ygdjhk evys1bk0","css-1plcdrk evys1bk0"])
        # paragraphs = soup.find_all('section', itemprop="articleBody") #more general but not accurate
        out_article = ""
        for p in paragraphs:
            out_article += (" "+ p.get_text())
        counter += 1

        # the print statement is to comparing the word count between official and own scraping,
        # to improve scraping accuracy
        print(str(counter) + "----------")
        print("official word count: " + str(each_a['word_count']))
        print("Web Scraping word count: " + str(len(out_article.split())))
        print(out_article)
        with open(filename, 'a', encoding='utf-8', newline="") as file:
            writer = csv.writer(file)
            writer.writerow([each_a['pub_date'], each_a['_id'], out_article, each_a['web_url']])

    # 5s break from each api call, avoid abusing the NYTimes api
    time.sleep(5)


if __name__ == '__main__':

    # taking the first 100 articles
    for page in range(10):
        getArticle(page, "basketball", 'nyt_basketball.csv')
    print("Done")
