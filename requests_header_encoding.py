import sys
import requests

url = sys.argv[1]
r = requests.get(url)
r_temp = r.text
r2 = r_temp.replace('\xa9','') #変換できない文字を置換
print(f'encoding: {r.encoding}',file=sys.stderr)
print(r2)

