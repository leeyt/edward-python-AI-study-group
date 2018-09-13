import requests

r = requests.get("http://www.flag.tw")

print(r.text)
print(r.encoding)

r = requests.get("http://www.flag.tw")

r.encoding = 'big5'
print(r.text)
print(r.encoding)