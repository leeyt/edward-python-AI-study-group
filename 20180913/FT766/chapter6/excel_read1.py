import xlwt  # Excel檔案讀取用
import xlrd  # Excel檔案寫入用

# --- Excel檔案的寫入
# 準備Work book
wb = xlwt.Workbook()
# 增加工作表（sheet）
ws = wb.add_sheet('工作表1')
# 在工作表的特定儲存格裡置入數值
ws.write(0, 0, 'Upper Left')
ws.write(1, 0, 1)
ws.write(1, 1, 2)
ws.write(1, 2, xlwt.Formula("A3+B3"))
# 將Work book命名並儲存
wb.save('xlwt.xls')

# --- Excel檔案的讀取
# 指定開啟要讀取的Work book
wb = xlrd.open_workbook('xlwt.xls')
# 以名稱指定工作表
st = wb.sheet_by_name('工作表1')
# 讀取並顯示指定工作表當中特定儲存格的數值
print(st.cell(0, 0).value)
