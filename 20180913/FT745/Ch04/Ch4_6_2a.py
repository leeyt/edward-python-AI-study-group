import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.flag.tw")
soup = BeautifulSoup(r.text, "lxml")

fp = open("flag2.txt", "w", encoding="utf8")
fp.write(soup.prettify())
print("寫入檔案flag2.txt...")
fp.close()



