#python C:\Users\User\Documents\GitHub\cycu_oop_11372003\20250408\3.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

def fetch_bus_list(driver):
    """
    抓取公車列表，讓使用者選擇公車。
    """
    try:
        # 等待公車列表載入完成
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[dognum]"))
        )

        # 抓取所有公車選項
        buses = driver.find_elements(By.CSS_SELECTOR, "a[dognum]")
        bus_list = []
        for bus in buses:
            bus_name = bus.text.strip()
            bus_route = bus.get_attribute("href").split("routeid=")[-1]
            bus_list.append((bus_name, bus_route))
            print(f"{len(bus_list)}. {bus_name} (Route ID: {bus_route})")

        # 讓使用者選擇公車
        choice = int(input("請選擇公車編號： ")) - 1
        if 0 <= choice < len(bus_list):
            return bus_list[choice][1]
        else:
            raise ValueError("無效的選擇")

    except Exception as e:
        print(f"發生錯誤：{e}")
        return None

def fetch_bus_route_data(driver, route_id):
    """
    抓取指定公車的站名和到站時刻，並輸出為 CSV 格式。
    """
    try:
        url = f"https://ebus.gov.taipei/Route/StopsOfRoute?routeid={route_id}"
        driver.get(url)
        time.sleep(2)  # 等待頁面加載

        # 等待站點列表載入完成
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ul.auto-list-pool.stationlist-list-pool"))
        )

        # 抓取所有站點資料
        stations = driver.find_elements(By.CSS_SELECTOR, "ul.auto-list-pool.stationlist-list-pool li")
        data = []
        for station in stations:
            stop_number = station.find_element(By.CLASS_NAME, "auto-list-stationlist-number").text.strip()
            stop_name = station.find_element(By.CLASS_NAME, "auto-list-stationlist-place").text.strip()
            stop_id = station.find_element(By.CSS_SELECTOR, "input[name='item.UniStopId']").get_attribute("value")
            latitude = station.find_element(By.CSS_SELECTOR, "input[name='item.Latitude']").get_attribute("value")
            longitude = station.find_element(By.CSS_SELECTOR, "input[name='item.Longitude']").get_attribute("value")
            arrival_info = station.find_element(By.CLASS_NAME, "auto-list-stationlist-position-time").text.strip()

            # 將資料加入列表
            data.append([arrival_info, stop_number, stop_name, stop_id, latitude, longitude])

        # 將資料寫入 CSV 檔案
        output_file = f"bus_route_{route_id}.csv"
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["arrival_info", "stop_number", "stop_name", "stop_id", "latitude", "longitude"])
            writer.writerows(data)

        print(f"資料已儲存至 {output_file}")

    except Exception as e:
        print(f"發生錯誤：{e}")

def main():
    """
    主程式，整合公車選擇與站點資料抓取。
    """
    # 初始化 WebDriver
    driver = webdriver.Chrome()

    try:
        # 打開公車列表頁面
        driver.get("https://ebus.gov.taipei/Route")
        time.sleep(2)  # 等待頁面加載

        # 抓取公車列表並讓使用者選擇
        route_id = fetch_bus_list(driver)
        if route_id:
            # 抓取選定公車的站點資料
            fetch_bus_route_data(driver, route_id)

    finally:
        # 關閉瀏覽器
        driver.quit()

if __name__ == "__main__":
    main()