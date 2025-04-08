from datetime import datetime

def calculate_julian_date(input_time_str):
    """
    計算輸入時間的星期幾及至今經過的太陽日數。
    
    :param input_time_str: 輸入時間字串，格式為 "YYYY-MM-DD HH:MM"
    :return: 該天是星期幾，以及至今經過的太陽日數
    """
    # 定義 Julian 日期的起始點
    JULIAN_START = datetime(4713, 1, 1, 12)  # 公元前4713年1月1日中午

    # 將輸入時間字串轉換為 datetime 物件
    input_time = datetime.strptime(input_time_str, "%Y-%m-%d %H:%M")

    # 計算該天是星期幾
    weekday = input_time.strftime("%A")  # 星期幾 (英文)

    # 計算輸入時間的 Julian 日期
    julian_date_input = (input_time - JULIAN_START).total_seconds() / 86400

    # 計算現在的 Julian 日期
    now = datetime.utcnow()
    julian_date_now = (now - JULIAN_START).total_seconds() / 86400

    # 計算輸入時間至今經過的太陽日數
    elapsed_days = julian_date_now - julian_date_input

    return weekday, elapsed_days

# 讓使用者輸入時間
input_time = input("請輸入時間 (格式為 YYYY-MM-DD HH:MM，例如 2020-04-15 20:30)： ")
try:
    weekday, elapsed_days = calculate_julian_date(input_time)
    print(f"輸入時間是星期：{weekday}")
    print(f"輸入時間至今經過的太陽日數：{elapsed_days:.6f}")
except ValueError:
    print("輸入的時間格式不正確，請使用 YYYY-MM-DD HH:MM 格式。")

#python C:\Users\User\Documents\GitHub\cycu_oop_11372003\20250408\2.py