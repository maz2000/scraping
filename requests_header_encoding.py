import sys
import requests

url = sys.argv[1]
r = requests.get(url)
r.encoding = r.apparent_encoding #文字化けのおまじない
r_temp = r.text
r2 = r_temp.replace('\xa9','') #変換できない文字を置換
#r3 = r2.replace('\x88','')
#print(f'encoding: {r2.encoding}',file=sys.stderr)
print(r2)

