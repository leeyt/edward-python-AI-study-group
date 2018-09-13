import pickle  # 標準函式庫pickle的匯入

# 準備要儲存的物件
mydata = [1, 2, 3]

# 將物件（mydata）儲存於檔案'pickle1.pickle'（副檔名可以不是.pickle）
with open('pickle1.pickle', 'wb') as f:
    pickle.dump(mydata, f)

# 從檔案'pickle1.pickle'裡取出資料代入dat
with open('pickle1.pickle', 'rb') as f:
    dat = pickle.load(f)
