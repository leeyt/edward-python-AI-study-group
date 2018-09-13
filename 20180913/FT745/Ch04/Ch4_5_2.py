import requests

r = requests.get("http://www.flag.tw")

fp = open("flag.txt", "w", encoding="utf8")
fp.write(r.text)
print("寫入檔案flag.txt...")
fp.close()

