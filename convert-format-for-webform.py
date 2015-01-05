#!/usr/bin/env python3
# convert-format-for-webform.py
# convert csv to a suitable format to the webform of tweet-maker website
import re
from glob import glob

def write_delimiter():
    f.write('\n')
    f.write('-' * 32)
    f.write('\n')


for file in glob('subtitles/*.csv'):

    col_num = 0
    # add items
    for line in open(file):
        l = line.rstrip().split(',')
        if not col_num:
            col_num = len(l)
            res = []
            for i in range(col_num):
                res.append([])

        for i in range(len(l)):     # process each item of each line
            if not l[i] == '':      # ignore if empty line
                res[i].append(l[i])
        
    # output text
    with open(file[:-4] + '-converted.txt', 'w') as f:
        # 診断結果テキスト
        title = re.search('/(.+)\.csv', file).group(1)
        subtitle = ''.join(['[RESULT{}]'.format(str(i+2)) for i in range(col_num)])
        result_text = '『{}』第[RESULT1]話「{}」（脚本: [USER]）'.format(title, subtitle)
        f.write(result_text)
        write_delimiter()

        # 話数リスト
        work_num = max([len(i) for i in res])
        f.write('\n'.join([str(i+1) for i in range(work_num, work_num*2)]))
        write_delimiter()
        
        # ワードリスト
        for i in range(len(res)):
            f.write('\n'.join(res[i]))
            write_delimiter()
