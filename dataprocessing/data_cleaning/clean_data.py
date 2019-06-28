# File Name: clean_data.py
# This program is use python spacy library to filter the texts in tweets, nyt and cc articles.
# Library spacy will filter out stop word and stem the word to the base form.
import csv
import re
import spacy
import os


# Method for Cleaning Data.
def clean_data(input_f, output_f, data_p, data_limit):
    nlp = spacy.load('en_core_web_sm') # Load spacy english library.
    with open(input_f, 'r', encoding='utf-8', errors='ignore') as csv_file_r: # Read texts From input file
        csv_r = csv.reader((line.replace('\0','') for line in csv_file_r))
        count = 0
        w_c = 0
        for data in csv_r:
            if count != 0 and count <= data_limit:
                data_s = re.sub(r'http\S+', '', data[data_p])  # Filter out web links
                data_s = re.sub(r'\W+', ' ', data_s)  # Filter out characters
                data_s = data_s.lower()  # Lowercase all to string
                data_t = nlp(data_s)  # nlp() is use to stem the words produce data_t as token
                c_data_n = []
                for w_s in data_t:  # For each token in data_t check its properties below
                    if w_s.is_stop: pass  # Filter out stop word
                    elif not w_s.is_alpha: pass  # Filter out word contains character
                    elif len(w_s.text) == 1: pass  # Filter out single letter
                    elif len(w_s.text) != 1 and len(w_s.lemma_) == 1: c_data_n.append(w_s.text)  # Restore the word such that its length is 1 after stem
                    else: c_data_n.append(w_s.lemma_)  # Store the stem word to list c_data_n
                with open(output_f, 'a', encoding='utf-8', newline="\n") as file_w:  # Store data to output file
                    w_c = w_c + len(c_data_n)
                    w_line = ' '.join(c_data_n)  # Convert the list to string with space
                    file_w.writelines(w_line + os.linesep)  # Write the list to the output file
            count = count + 1
    return w_c


# The dic contains all common crawls data from each topics
dictCC = ["cc_data/cc_sport.csv", "cc_data/cc_basketball.csv",
          "cc_data/cc_baseball.csv", "cc_data/cc_football.csv", "cc_data/cc_soccer.csv"]

# The dic contains all new york time data from each topics
dictNYT = ["nyt_data/nyt_sport.csv", "nyt_data/nyt_basketball.csv",
           "nyt_data/nyt_baseball.csv", "nyt_data/nyt_football.csv", "nyt_data/nyt_soccer.csv"]

# The dic contains all tweeter data from each topics
dictTW = ["tw_data/tw_sport.csv", "tw_data/tw_basketball.csv",
          "tw_data/tw_baseball.csv", "tw_data/tw_football.csv", "tw_data/tw_soccer.csv"]

dictInput = [dictCC, dictNYT, dictTW]  # Input dict
dictOut_all = ["cc_data/cc_all_cd.txt", "nyt_data/nyt_all_cd.txt", "nyt_data/nyt_all_cd.txt"]  # Output dict for path
dictOut_one = ["cc_data/cc_one_cd.txt", "nyt_data/nyt_one_cd.txt", "tw_data/tw_one_cd.txt"]
dictPos = [0, 2, 2]  # Position of text in each data
dictLim_all = [10000, 10000, 10000]
dictLim_one = [20, 20, 1000]

# Clean All data in each sources and store in dictOut files
for inputF, outputF, pos, lim in zip(dictInput, dictOut_one, dictPos, dictLim_one):
    w_c = 0
    for inF in inputF:
        w_c = w_c + clean_data(inF, outputF, pos, lim)
    print("Cleaned Data in " + outputF + " :" + str(w_c))
    print("-------------------------------------------")
print("Done")

