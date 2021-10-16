#!/usr/bin/python

'''
Import the "re" module for regular expression.
Open the file using the open() function.
Read all the lines in the file and store them in a list.
Declare the patter for IP addresses. The regex pattern is :

'''
import re


def extract_ip_address(data):
    lst = []
    with open(data, 'r') as file:
        fstring = file.readlines()

    for line in fstring:
        ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
        for ip in ips:
            lst.append(ip)
    return lst


print(extract_ip_address('data.log'))
