#!/usr/bin/env python

import requests

def request(url):
    try:
        return request.get("http://" + url)
    except request.exceptions.ConnectionError:
        pass


target_url = "google.com"

with open("D:\'01 proffessional'\vs\crawler\wordlist.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print(test_url)
