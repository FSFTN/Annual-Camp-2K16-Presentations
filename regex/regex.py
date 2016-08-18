#!/usr/bin/python

import sys
import re


filename = sys.argv[1]
pat = sys.argv[2]

for word in open(filename, 'r').readlines():
    if re.search(pat, word):
        print(word)
