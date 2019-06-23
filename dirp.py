#!/usr/bin/python3

import os
import sys
import requests
import time

def loadWordlist():
    # check wordlist
    if os.path.isfile(wordlist) == False:
        sys.exit('ERROR: ' + wordlist + ' does not exist')
    else:
        wordFile = open(wordlist, 'r', encoding = "ISO-8859-1")
        words = wordFile.read().splitlines()
        print('Wordlist loaded: ' + wordlist)

    return words

def checkBaseURL():
    # check baseurl
    req = requests.get(url)

    if req.status_code == requests.codes.ok:
        print('Successful connection to: ' + url)
    else:
        print('FAILED TO CONNECT')
        print('ERROR CODE: ' + str(req.status_code))

def startScan(words):
    print()
    print('<<< STARTING SCAN >>>')
    print()
    
    for i in words:
        req = requests.get(url + i)
        if req.status_code == requests.codes.ok:
            print(str(req.status_code) + ' ' + url + i)

# check command line arguments
if len(sys.argv) != 3:
    sys.exit('USAGE: dirp.py <http://baseurl/> <wordlist.txt>')

# load command line arguments
url = sys.argv[1]
wordlist = sys.argv[2]

words = loadWordlist()
checkBaseURL()
startScan(words)
