import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import csv
import os
import folium

async def find_bus():
    route_id = input("請告訴我公車代碼：").strip()
    url = f"https://ebus.gov.taipei/Route/StopsOfRoute?routeid={route_id}"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)

        try:
            await page.wait_for_selector("div#GoDirectionRoute li", timeout=10000)
        except:
            print("網頁載入超時，請確認公車代碼是否正確。")
            return

        html = await page.content()
        await browser.close()

    soup = BeautifulSoup(html, "html.parser")
    station_items = soup.select("div#GoDirectionRoute li")

    if not station_items:
        print("未找到任何站牌資料，請確認公車代碼是否正確。")
        return

    all_stations = []

    for idx, li in enumerate(station_items, start=1):
        try:
            spans = li.select("span.auto-list-stationlist span")
            inputs = li.select("input")

            stop_time = spans[0].get_text(strip=True)
            stop_number = spans[1].get_text(strip=True)
            stop_name = spans[2].get_text(strip=True)

            stop_id = inputs[0]['value']
            latitude = float(inputs[1]['value'])
            longitude = float(inputs[2]['value'])

            station = [stop_time, stop_number, stop_name, stop_id, latitude, longitude]
            all_stations.append(station)

        except Exception as e:
            print(f"第 {idx} 筆資料處理錯誤：{e}")

    if not all_stations:
        print("沒有成功抓取到任何站牌資訊。")
        return

    # 儲存結果到桌面上的 CSV
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_file = os.path.join(desktop_path, f"bus_information_{route_id}.csv")
    
    with open(output_file, mode="w", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["到站時間", "站牌編號", "站牌名稱", "站牌ID", "緯度", "經度"])
        writer.writerows(all_stations)

    print(f"\n抓到的站牌資訊已儲存至 {output_file}")
    print("\n抓到的站牌資訊如下：\n")
    for station in all_stations:
        print(", ".join(map(str, station[:-1])))  # 顯示時省略 raw_html，並將所有元素轉為字串

    # 繪製地圖
    draw_map(all_stations, route_id)

def draw_map(stations, route_id):
    """
    使用 Folium 繪製公車路線地圖
    """
    # 建立地圖，中心點為第一個站牌
    m = folium.Map(location=[stations[0][4], stations[0][5]], zoom_start=13)

    # 加入站牌標記
    for station in stations:
        folium.Marker(
            location=[station[4], station[5]],
            popup=f"{station[2]} ({station[1]})",
        ).add_to(m)

    # 儲存地圖到桌面
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    map_file = os.path.join(desktop_path, f"bus_route_map_{route_id}.html")
    m.save(map_file)
    print(f"互動地圖已儲存至 {map_file}")

# 執行主程式
if __name__ == "__main__":
    asyncio.run(find_bus())