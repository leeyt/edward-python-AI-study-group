import time
import requests
import csv
from bs4 import BeautifulSoup

# 目標URL網址
URL = "http://search.books.com.tw/search/query/key/{0}/cat/all"

def generate_search_url(url, keyword):
    url = url.format(keyword)
    
    return url

def get_resource(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
               "AppleWebKit/537.36 (KHTML, like Gecko)"
               "Chrome/63.0.3239.132 Safari/537.36"}
    return requests.get(url, headers=headers)

def parse_html(r):
    if r.status_code == requests.codes.ok:
        r.encoding = "utf8"
        soup = BeautifulSoup(r.text, "lxml")        
    else:
        print("HTTP請求錯誤..." + url)
        soup = None
    
    return soup   

def get_ISBN(url):
    soup = parse_html(get_resource(url))
    if soup != None:
        return soup.find(itemprop="productID")["content"][5:]
    else:
        return None
    
def get_prices(isbn):
    price1, price2 = None, None
    # 誠品
    url1 = "http://www.eslite.com/Search_BW.aspx?query="+isbn
    soup = parse_html(get_resource(url1))
    if soup != None:
        price1 = soup.find_all("span", class_="price_sale")[2].text
    else:
        price1 = None
    # 金石堂   
    url2 = "https://www.kingstone.com.tw/search/result.asp?c_name={0}&se_type=4"
    soup = parse_html(get_resource(url2.format(isbn)))
    if soup != None:
        price2 = soup.find("span", class_="sale_price").text
    else:
        price2 = None
        
    return price1, price2  

def save_to_csv(booklist, file):
    with open(file, 'w+', newline='') as fp:
        writer = csv.writer(fp)
        for book in booklist:
            writer.writerow(book)  

def web_scraping_bot(url):
    booklist = []
    print("抓取網路資料中...")
    soup = parse_html(get_resource(url))
    if soup != None:
        # print(soup)
        tag_item = soup.find_all(class_="item")
        for item in tag_item:
            book = []
            book.append(item.find("img")["alt"])
            isbn = get_ISBN(item.find("a")["href"])
            book.append(isbn)
            price = item.find(class_="price").find_all("b")
            book.append(price[1].string + "元")
            price1, price2 = get_prices(isbn)
            book.append(price1)
            book.append(price2)
            booklist.append(book)
            print("等待2秒鐘...")
            time.sleep(2) 

    return booklist

if __name__ == '__main__':
    url = generate_search_url(URL, "Python")
    print(url)
    booklist = web_scraping_bot(url)
    for item in booklist:
        print(item)
    save_to_csv(booklist, "booklist2.csv")
