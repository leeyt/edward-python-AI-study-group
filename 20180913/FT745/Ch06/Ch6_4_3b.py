import sqlite3

d = {
   "id": "P0003",
   "title": "Node.js程式設計",
   "price": 650
}

# 建立資料庫連接
conn = sqlite3.connect("Books.sqlite")
# 建立SQL指令INSERT字串
sql = "INSERT INTO Books (id, title, price) VALUES ('{0}','{1}',{2})"
sql = sql.format(d['id'], d['title'], d['price'])
print(sql)
cursor = conn.execute(sql)   # 執行SQL指令
print(cursor.rowcount)
conn.commit() # 確認交易
conn.close()  # 關閉資料庫連接

