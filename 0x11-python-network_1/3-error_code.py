#!/usr/bin/python3
'''Python script that fetches https://alx-intranet.hbtn.io/status'''
import urllib.request
import urllib.parse
import urllib.error
import sys

if __name__ == "__main__":
    '''the script definition'''
    # url = 'https://alx-intranet.hbtn.io/status'
    url = sys.argv[1]
    quest = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(quest) as response:
            page = response.read()
            page_ = page.decode('utf-8')
            print(page_)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
