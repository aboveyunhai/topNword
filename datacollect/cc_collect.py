from time import time
import warc
from newspaper import Article
import csv
import wget
import pprint

# example common crawl link for news from amazonAWA
# url = "https://commoncrawl.s3.amazonaws.com/crawl-data/CC-NEWS/2019/03/CC-NEWS-20190324002911-00036.warc.gz"
# url = "https://commoncrawl.s3.amazonaws.com/crawl-data/CC-NEWS/2019/03/CC-NEWS-20190327033922-00059.warc.gz"
# file_name = wget.download(url)

# infile = "CC-NEWS-20190324002911-00036.warc.gz"
# infile = "CC-NEWS-20190327033922-00059.warc.gz"

# desitination file 
# outfile = ".csv"

"""
example topic and keyword for fetch desired article from websites
topic:{sport, basketball, soccer, football, baseball}
keyword: depends on your topic, keyword is critical, it might increase or reduce the accuracy of data 
 
"""

topic = 'soccer'
topic_keywords = {'soccer', 'Soccer', 'FIFA', 'World Cup'}

# read article from website
# return None if the article is not desired language
def read_doc(record):
    url = record.url
    article = None
    if url:
        article = Article(url, language="en")
    return url, article

# process Common Crawl file and extract url from source
def process_warc(infile, outfile, limit):
    warc_file = warc.open(infile, 'rb')
    t0 = time()
    n_websites = 0
    n_documents = 0
    for record in warc_file:
        url, doc = read_doc(record)

        # check if the doc with specific language exist
        if url and doc:

            # mainly catch timeout exception if unable to extract article from unknown urls
            # and other possible exceptions from unknown url
            try:
                doc.download()
                doc.parse()
            except:
                continue

            # check if the doc relates to the topic
            if topic in url or any(x in doc.text for x in topic_keywords):
                with open(outfile, 'a', encoding='utf-8', newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([doc.text, url])
                n_documents += 1
                print("WebLink %s: %s" % (n_documents, url))

        n_websites += 1
        print(n_websites)

        # exit function if we contains enough articles or excesses the given limit of website search
        if n_documents >= 120 or n_websites > limit:
            break

    warc_file.close()
    print('Parsing took %s seconds, produced %s websites and %s documents' % (time() - t0, n_websites -1, n_documents))


if __name__ == '__main__':
    process_warc(infile, outfile,100000)
    print("Done")