#!/usr/bin/env python3
# convert-format-for-webform.py
# convert csv to a suitable format to the webform of tweet-maker website

res = []
for i in range(4):
    res.append([])

# add items
for line in open('subtitles.csv'):
    l = line.rstrip().split(',')
    for i in range(len(l)):     # process each item of each line
        if not l[i] == '':      # ignore if empty line
            res[i].append(l[i])
    
# output text
with open('subtitles-converted.csv', 'w') as f:
    for i in range(len(res)):
        f.write('\n'.join(res[i]))
        f.write('\n')
        f.write('-' * 32)
        f.write('\n')
