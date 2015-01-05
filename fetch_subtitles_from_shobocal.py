#!/usr/bin/env python3
# fetch_subtitles_from_shobocal.py
#   しょぼいカレンダーのデータからサブタイトルリストを生成するプログラム
import json
import requests
import sys

def convert_key_to_int(d):
    new_d = {}
    for k, v in d.items():
        new_d[int(k)] = v
    return new_d

if len(sys.argv) != 2 or not int(sys.argv[1]) > 0:
    print('しょぼいカレンダー(http://cal.syoboi.jp/)のTID(番組のID番号)を引数に指定してください。')
    sys.exit()
else:
    tid = sys.argv[1]

r = requests.get('http://cal.syoboi.jp/json.php?Req=SubTitles,TitleMedium&TID=' + tid)

title = json.loads(r.text)['Titles'][tid]['Title']
subtitles = json.loads(r.text)['SubTitles'][tid]
subtitles = convert_key_to_int(subtitles)

filename = 'subtitles/' + title + '.txt'
with open(filename, 'w') as f:
    for num, subtitle in subtitles.items():
        f.write(subtitle + '\n')
    print('Wrote', filename)
