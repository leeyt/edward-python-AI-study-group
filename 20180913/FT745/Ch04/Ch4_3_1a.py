import requests

r = requests.get("http://www.flag.tw")
print(r.text)
print("----------------------")

r = requests.get("http://www.flag.tw")
print(r.content)
print("----------------------")

r = requests.get("http://www.flag.tw", stream=True)
print(r.raw)
print(r.raw.read(15))

