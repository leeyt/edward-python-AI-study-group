import time
import requests
import json

# 目標 REST API 網址
URL = "https://api.hahow.in/api/courses?category="
CATEGORY = "55de81ac9d1fa51000f94770"    # 課程分類

def get_json(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
               "AppleWebKit/537.36 (KHTML, like Gecko)"
               "Chrome/63.0.3239.132 Safari/537.36"}
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        r.encoding = "utf8"
        json_data = r        
    else:
        print("HTTP請求錯誤..." + url)
        json_data = None
    
    return json_data    

def save_to_json(courselist, file):
    with open(file, "w", encoding="utf-8") as fp:
        json.dump(courselist, fp, indent=2, sort_keys=True, ensure_ascii=False)
            
def web_scraping_bot(url):
    courselist = []
    print("抓取REST API的JSON資料中...")
    resp_courses = get_json(url + "&limit=12&status=PUBLISHED").json()
    while resp_courses:  # 有回傳資料則繼續抓
        print("等待2秒鐘...")
        time.sleep(2)  # 放慢爬蟲速度
        courselist += resp_courses
        param = "&latestId={0}&latestValue={1}&limit=12&status=PUBLISHED".format(
            courselist[-1]["_id"], courselist[-1]["incubateTime"])
        print(url + param)
        resp_courses = get_json(url + param).json()

    return courselist

if __name__ == '__main__':
    url = URL + CATEGORY
    print(url)
    courselist = web_scraping_bot(url)
    for item in courselist:
        print(item["title"])
    save_to_json(courselist, "courselist.json")
