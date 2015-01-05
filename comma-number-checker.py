#!/usr/bin/env python3
# comma-number-checker.py
# check whether every line has the same number of commas(,)

import itertools
from glob import glob

for file in glob('subtitles/*.csv'):
    target = 0
    print(file)
    for i, line in zip(itertools.count(1), open(file)):
        commas = line.count(',')
        if not target:
            target = commas
        if not commas == target:
            print(i, commas)
