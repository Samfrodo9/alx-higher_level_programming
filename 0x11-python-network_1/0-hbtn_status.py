#!/usr/bin/python3

"""a Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    '''the script definition'''
    url = 'https://alx-intranet.hbtn.io/status'
    quest = urllib.request.Request(url)
    with urllib.request.urlopen(quest) as response:
        page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode("utf-8")))
