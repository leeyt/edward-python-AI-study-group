from bs4 import BeautifulSoup

with open("flag.txt", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    print(soup.prettify())



