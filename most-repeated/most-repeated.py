#! /usr/bin/python
# Take a paragraph as Input and output the top three most repeated words
# for word in `cat paragraph.txt`; do echo $word; done | sort | uniq -c | sort -nr | head -3
from collections import Counter

def most_reapeated_words(file):
    wordlist = []
    try:
        with open(file, 'r') as file:
            for line in file:
                words = line.strip().lower().replace(',', '.').split(" ")
                for word in words:
                    wordlist.append(word)
        c = Counter(wordlist)
        print(c.most_common(3))
    finally:
        file.close()


most_reapeated_words('paragraph.txt')
