#!/usr/bin/python3

"""A python script that sends a request to a URL"""

import urllib.request
import sys

if __name__ == "__main__":
	'''The script definition'''
	url = sys.argv[1]
	with urllib.request.urlopen(url) as site:
		info_dict = site.info()
		print(info_dict['X-Request-ID'])
