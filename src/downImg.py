import csv
import requests
import os
from os import listdir



data = {}

# download the pics
def request_download(oss, url):
    r = requests.get(url)
    with open("../round1_test3/"+str(oss) + ".jpg", "wb") as f:
        f.write(r.content)

# open csv file to extract urls
with open('../Xeon1OCR_round1_test3_20210528.csv', 'r', encoding='utf-8') as f:
    url_list = []
    url = ""
    reader = csv.reader(f)
    for row in reader:
        url = row[1][13:-2]
        # print(url)
        url_list.append(row[1][13:-2])

for oss in range(len(url_list)-1):
    oss = oss + 1
    request_download(oss, url_list[oss])
    print(url_list[oss])