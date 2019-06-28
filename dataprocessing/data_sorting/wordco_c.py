import csv
import os


def wordcc(article, list_tt):
    artF = article.split()
    list_wcc = []
    for item in list_tt:
        indexes = [i for i, s in enumerate(artF) if item == s]
        for index in indexes:
            s_tmp_l = item + "+" + artF[index - 1]
            list_wcc.append(s_tmp_l)
            if index != len(artF)-1:
                s_tmp_r = item + "+" + artF[index + 1]
                list_wcc.append(s_tmp_r)
    return list_wcc


def topten_w(fileN_tt):
    with open(fileN_tt, 'r', encoding='utf-8') as file_r_c:
        readFC = csv.reader(file_r_c)
        list_t = []
        count = 0
        for w in readFC:
            if count != 0:
                list_t.append(w[0])
            count += 1
    return list_t


def word_cc_a(fileN, fileN_t, inputF):
    listN_tt = topten_w(fileN_t)
    with open(fileN, 'r', encoding='utf-8') as file_r:
        readF = file_r.readlines()
        w_c = 0
        list_result = []
        for s in readF:
            list_tt = wordcc(s, listN_tt)
            print(list_tt)
            w_c = w_c + len(list_tt)
            with open(inputF, 'a', encoding='utf-8', newline='\n') as file_w:
                w_line = ' '.join(list_tt)
                file_w.writelines(w_line + os.linesep)
    return w_c


word_cc_a('tw_data/tw_all_cd.txt', 'tw_data/tw_tt.csv', 'tw_data/tw_wcc_all.txt')

# print(wordcc(largestFile('nyt_data/nyt_all_cd.txt'), topten_w('nyt_data/nyt_tt.csv')))
