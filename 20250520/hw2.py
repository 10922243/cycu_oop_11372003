import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 讀取資料
df = pd.read_csv('20250520/midterm_scores.csv')

# 定義科目及顏色
subjects = ['Chinese', 'English', 'Math', 'History', 'Geography', 'Physics', 'Chemistry']
colors = ['red', 'orange', 'yellow', 'green', 'skyblue', 'blue', 'purple']

# 定義分數範圍
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
bin_centers = [(bins[i] + bins[i+1]) / 2 for i in range(len(bins) - 1)]  # 計算每個區間的中心點

# 計算每個科目在各分數區間的人數
width = 1 / (len(subjects) + 1)  # 每個柱狀圖的寬度
x_offsets = np.arange(len(bin_centers))  # X 軸的基準位置

plt.figure(figsize=(12, 8))

for i, (subject, color) in enumerate(zip(subjects, colors)):
    # 計算每個分數區間的人數
    counts, _ = np.histogram(df[subject], bins=bins)
    # 繪製柱狀圖，並將每個科目分開
    plt.bar(x_offsets + i * width, counts, width=width, label=subject, color=color, edgecolor='black')

# 圖表設定
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.title('Distribution of Scores by Subject (Side-by-Side)')
plt.xticks(x_offsets + (len(subjects) - 1) * width / 2, [f"{bins[i]}-{bins[i+1]-1}" for i in range(len(bins) - 1)], rotation=45)
plt.legend(title='Subjects')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# 顯示圖表
plt.show()