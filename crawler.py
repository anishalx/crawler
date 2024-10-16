#!/usr/bin/env python

import requests

def request(url):
    try:
        return requests.get("https://" + url, timeout=5) 
    except requests.exceptions.ConnectionError:
        return None 
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}") 

target_url = "google.com"

with open("/home/kali/vs/crawler/wordlist.list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print(test_url)
