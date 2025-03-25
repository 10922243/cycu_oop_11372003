import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV 檔案，嘗試不同的編碼格式
file_path = r'c:\Users\User\Documents\GitHub\cycu_oop_11372003\20250325\ExchangeRate@202503251948.csv'
data = pd.read_csv(file_path, encoding='utf-8-sig')

# 確保欄位名稱正確，移除可能的空格或隱藏字符
data.columns = data.columns.str.strip()

# 檢查資料是否正確，過濾掉非日期的資料
data = data[pd.to_numeric(data['資料日期'], errors='coerce').notna()]

# 將資料日期轉換為日期格式
data['資料日期'] = pd.to_datetime(data['資料日期'], format='%Y%m%d')

# 選取需要的欄位
data = data[['資料日期', '現金', '現金2']]

# 繪製折線圖
plt.figure(figsize=(10, 6))
plt.plot(data['資料日期'], data['現金'], label='現金', color='blue')
plt.plot(data['資料日期'], data['現金2'], label='現金2', color='red')

# 設定中文字型
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 設定圖表標題與軸標籤
plt.title('現金與現金2匯率折線圖')
plt.xlabel('日期')
plt.ylabel('匯率')
plt.legend()

# 顯示圖表
plt.grid()
plt.show()