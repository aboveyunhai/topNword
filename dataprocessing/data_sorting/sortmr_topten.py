# File Name: sortmr_topten.py
# This program is use to sort the output after MapReduce, find the top ten word, and store in the csv for Tablue
import csv


# Method for sorting and storing
def findtopwords(filen, outputF):
    filename = filen
    with open(filename, 'r', encoding='utf-8') as file:  # Read MapReduce Output <key, value> and store to dictionary
        readF = file.readlines()
        dicF = {}
        for r in readF:
            tmp = r.split()
            tmp_d = tmp[0].split('+')
            tmp_d = [k for k in sorted(tmp_d)]
            tmp_dr = '+'.join(tmp_d)
            if tmp_dr in dicF:
                dicF[tmp_dr] = dicF[tmp_dr] + int(tmp[1])   # Produce dict such that in format of dict[key] = value
            else:
                dicF[tmp_dr] = int(tmp[1])

        c = 1
        print("Top Ten Word in " + filename + ":")
        for key, value in sorted(dicF.items(), key=lambda item: item[1], reverse=True):  # Sorting by value, Algorithm provided by python library

            if c <= 10:
                print("%s. %s: %s" % (c, key, value))
                with open(outputF, 'a', encoding='utf-8', newline='') as file_w:  # Store the top ten word to output csv
                    writer = csv.writer(file_w)
                    writer.writerow([key, value])
                c += 1


# Method for create header for output csv file in format of [keyword, frequency]
def header(filename):
    with open(filename, 'a', encoding='utf-8', newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["keyword", "frequency"])


# Paths: Input File with WCC and without WCC, Output File with WCC and without WCC
dictInput = ["cc_data/cc_all_mr.txt", "nyt_data/nyt_all_mr.txt", "tw_data/tw_all_mr.txt"]
dictInput_One = ["cc_data/cc_one_mr.txt", "nyt_data/nyt_one_mr.txt", "tw_data/tw_one_mr.txt"]
dictInputW = ["cc_data/cc_wcc_mr.txt", "nyt_data/nyt_wcc_mr.txt", "tw_data/tw_wcc_mr.txt"]
dictOut = ["cc_data/cc_tt.csv", "nyt_data/nyt_tt.csv", "tw_data/tw_tt.csv"]
dictOut_One = ["cc_data/cc_one_tt.csv", "nyt_data/nyt_one_tt.csv", "tw_data/tw_one_tt.csv"]
dictOutW = ["cc_data/cc_wcc_tt.csv", "nyt_data/nyt_wcc_tt.csv", "tw_data/tw_wcc_tt.csv"]

# For input and output without WCC
# for inputF, outputF in zip(dictInput, dictOut):
#     header(outputF)
#     findtopwords(inputF, outputF)

# For input and output with WCC
for inputF, outputF in zip(dictInputW, dictOutW):
    header(outputF)
    findtopwords(inputF, outputF)
#
# for inputF_one, outputF_one in zip(dictInput_One, dictOut_One):
#     header(outputF_one)
#     findtopwords(inputF_one,outputF_one)