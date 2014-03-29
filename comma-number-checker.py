#!/usr/bin/env python3
# comma-number-checker.py
# check whether every line has 3 comma(,)
# カンマの数が合っているか不安だったので、itertoolsの使いかたの勉強を兼ねて書きました。

import itertools

for i, line in zip(itertools.count(), open('subtitles.csv')):
    commas = line.count(',')
    if not commas == 3:
        print(i, commas)
