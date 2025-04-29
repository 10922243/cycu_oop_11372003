import folium
import os
from folium import CustomIcon
from folium import PolyLine

def draw_map(stations, route_id):
    """
    使用 Folium 繪製公車路線地圖，並在指定站牌上放置小人.png 和公車.png，並繪製去程或回程路線
    """
    # 讓使用者選擇去程或回程
    direction = input("請輸入去程(輸入'0')或回程(輸入'1')：").strip()
    if direction not in ["0", "1"]:
        print("輸入錯誤，請輸入'0'或'1'")
        return

    # 建立地圖，中心點為第一個站牌
    m = folium.Map(location=[stations[0][4], stations[0][5]], zoom_start=13)

    # 加入站牌標記
    route_coordinates = []  # 用於存儲路線的經緯度
    for station in stations:
        # 如果到站時間為 "進站中"，使用公車.png
        if station[0] == "進站中":
            bus_icon_path = r"C:\Users\User\Desktop\cycu_oop_11372003\20250429\公車.png"
            if not os.path.exists(bus_icon_path):
                print(f"找不到圖片檔案：{bus_icon_path}")
                continue

            bus_icon = CustomIcon(icon_image=bus_icon_path, icon_size=(30, 30))
            # 將公車圖示放置在站牌位置的右邊（經度 + 0.0005）
            folium.Marker(
                location=[station[4], station[5] + 0.0005],
                popup=f"公車進站中：{station[2]} ({station[1]})",
                icon=bus_icon
            ).add_to(m)

        # 一般站牌標記
        folium.Marker(
            location=[station[4], station[5]],
            popup=f"{station[2]} ({station[1]})",
        ).add_to(m)

        # 將站牌的經緯度加入路線座標
        route_coordinates.append((station[4], station[5]))

    # 繪製路線
    PolyLine(
        locations=route_coordinates,
        color="blue" if direction == "0" else "red",  # 去程為藍色，回程為紅色
        weight=5,
        opacity=0.8,
        tooltip=f"公車路線：{route_id} (去程)" if direction == "0" else f"公車路線：{route_id} (回程)"
    ).add_to(m)

    # 讓使用者輸入站牌編號
    target_station_number = input("請輸入要放置小人的站牌編號：").strip()

    # 搜尋目標站牌
    for station in stations:
        if station[1] == target_station_number:
            # 使用 CustomIcon 放置小人.png
            icon_path = r"C:\Users\User\Desktop\cycu_oop_11372003\20250429\小人.png"
            if not os.path.exists(icon_path):
                print(f"找不到圖片檔案：{icon_path}")
                return

            custom_icon = CustomIcon(icon_image=icon_path, icon_size=(30, 30))
            folium.Marker(
                location=[station[4], station[5]],
                popup=f"小人位置：{station[2]} ({station[1]})",
                icon=custom_icon
            ).add_to(m)
            print(f"已在站牌編號 {station[1]} 放置小人.png")
            break
    else:
        print("未找到指定的站牌編號，請確認輸入是否正確。")

    # 儲存地圖到桌面
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    map_file = os.path.join(desktop_path, f"bus_route_map_{route_id}_gb{direction}.html")
    m.save(map_file)
    print(f"互動地圖已儲存至 {map_file}")