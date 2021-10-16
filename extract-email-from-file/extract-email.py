#!/usr/bin/python

import re


def extract_emails(file):
    try:
        lst = []
        with open(file, 'r') as file:
            lines = file.readlines()
        for line in lines:
            lst.append(re.findall('\S+@\S+', line))

        for email in lst:
            if len(email) != 0:
                return email
    finally:
        file.close()


print(extract_emails('email-file.txt'))
