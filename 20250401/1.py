from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 初始化 WebDriver
driver = webdriver.Chrome()

try:
    # 打開目標網站
    driver.get("https://pda5284.gov.taipei/MQS/route.jsp?rid=10417")
    time.sleep(2)  # 等待頁面加載

    # 輸入站名
    station_name = input("請輸入公車站名 (例如: 蘆洲總站): ")

    # 等待並定位站名的超連結
    station_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, station_name))  # 使用站名文字定位
    )
    station_element.click()  # 點擊站名超連結
    time.sleep(2)  # 等待資料加載

    # 定義需要讀取的 class 名稱
    class_names = ["ttego1", "ttego2", "tteback1", "ttwback2"]

    # 遍歷 class 名稱並讀取對應的元素
    for class_name in class_names:
        elements = driver.find_elements(By.CLASS_NAME, class_name)
        for element in elements:
            print(f"Class: {class_name}, Text: {element.text}")

finally:
    # 關閉瀏覽器
    driver.quit()

#python C:\Users\User\Desktop\cycu_oop_11372003\20250401\1.py