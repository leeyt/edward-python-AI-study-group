from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 測試取出<li>標籤的內容
tag_li = soup.find(class_="response")
print(tag_li.string)
print(tag_li.span.string)

