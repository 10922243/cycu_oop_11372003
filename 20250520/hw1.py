import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv('c:/Users/User/Documents/GitHub/cycu_oop_11372003/20250520/midterm_scores.csv')

# 定義科目
subjects = ['Chinese', 'English', 'Math', 'History', 'Geography', 'Physics', 'Chemistry']

# 計算每位學生不及格的科目數量
df['FailCount'] = df[subjects].apply(lambda row: (row < 60).sum(), axis=1)

# 找出不及格科目超過半數的學生
threshold = len(subjects) // 2  # 超過半數的門檻
students_with_many_fails = df[df['FailCount'] > threshold]

# 輸出結果
print("超過半數科目不及格的學生：")
print(students_with_many_fails[['Name', 'StudentID', 'FailCount']])

# 將結果輸出為 CSV 檔案
output_path = 'c:/Users/User/Documents/GitHub/cycu_oop_11372003/20250520/hw1_students_with_many_fails.csv'
students_with_many_fails[['Name', 'StudentID', 'FailCount']].to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"結果已輸出至 {output_path}")