#!/usr/bin/python3

#
# def listToString(s):
#     for elem in s:
#         return ' '.join([str(elem) for elem in s])
#
#
# s2 = ['I', 'want', 5, 'apples', 'and', 18, 'bananas']
# print(listToString(s2))

import requests
from bs4 import BeautifulSoup

url = 'https://www.geeksforgeeks.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

def extract_url(url):
    try:
        urls = []
        f = open('url-links.txt', 'w')
        for link in soup.find_all('a'):
            data = link.get('href')
            f.write(data)
            f.write('\n')
    finally:
        f.close()

extract_url(url)
