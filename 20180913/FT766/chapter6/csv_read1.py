import csv # 匯入標準模組csv使用


# CSV檔案的讀取
with open('data1.csv', 'r', encoding='utf8') as f:
    dat = [k for k in csv.reader(f)] # 使用list comprehension

# CSV檔案的寫入
with open('out.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(dat)
