'''
this script is used for creating csv file for _collect.py to store
the csv header depends on the source

'''
import csv

topic_name = ""
        
def tweet_header(topic_name):
    filename = "tw_" + topic_name
    with open(filename, 'a', encoding='utf-8', newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["created_at", "id", "text"])


def nyt_header(topic_name):
    filename = "nyt_" + topic_name
    with open(filename, 'a', encoding='utf-8', newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["pub_date", "id", "text", "web_url"])


def cc_header(topic_name):
    filename = "cc_" + topic_name
    with open(filename, 'a', encoding='utf-8', newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["text", "web_url"])


if __name__ == '__main__':
    # tweet_header(topic_name)
    # nyt_header(topic_name)
    # cc_header(topic_name)
    print("Add Header Done")
