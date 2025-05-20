import os
import sys
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString
from matplotlib.colors import ListedColormap
import pandas as pd

# 確保模組路徑正確
project_path = 'c:/Users/User/Documents/GitHub/cycu_oop_11372003/'
if project_path not in sys.path:
    sys.path.append(project_path)

class BusRouteMap:
    def __init__(self, route_id, direction, route_info_class):
        self.route_id = route_id
        self.direction = direction
        self.route_info_class = route_info_class
        self.route_data = None
        self.geometry = None

    def fetch_route_data(self):
        """取得公車路線資料"""
        route_info = self.route_info_class(self.route_id, direction=self.direction)
        route_info.parse_route_info()
        self.route_data = route_info.dataframe

    def create_geometry(self):
        """將站牌資料轉換為地理幾何資料"""
        if self.route_data is None:
            raise ValueError("Route data is not fetched. Call fetch_route_data() first.")
        
        # 建立站牌的點資料
        self.route_data['geometry'] = self.route_data.apply(
            lambda row: Point(row['longitude'], row['latitude']), axis=1
        )
        # 建立路線的線資料
        self.geometry = LineString(self.route_data['geometry'].tolist())

    def plot_route(self, base_map=None):
        """繪製公車路線"""
        if self.geometry is None:
            raise ValueError("Geometry is not created. Call create_geometry() first.")
        
        # 建立 GeoDataFrame
        route_gdf = gpd.GeoDataFrame(self.route_data, geometry='geometry')
        line_gdf = gpd.GeoDataFrame([{'geometry': self.geometry}], crs="EPSG:4326")

        # 繪製地圖
        plt.figure(figsize=(12, 8))
        if base_map is not None:
            base_map.plot(ax=plt.gca(), color='lightgrey', edgecolor='black')
        route_gdf.plot(ax=plt.gca(), color='blue', markersize=50, label='Bus Stops')
        line_gdf.plot(ax=plt.gca(), color='red', linewidth=2, label='Bus Route')
        
        plt.title(f"Bus Route: {self.route_id} ({self.direction})", fontsize=16)
        plt.legend()
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

def load_base_map():
    """載入台北、新北、基隆、桃園地圖"""
    shp_dir = "20250520/taiwan_map"
    shp_file = None
    for fname in os.listdir(shp_dir):
        if fname.endswith(".shp"):
            shp_file = os.path.join(shp_dir, fname)
            break

    if shp_file is None:
        raise FileNotFoundError(f"No shapefile found in {shp_dir}")

    # 讀取 shapefile
    gdf = gpd.read_file(shp_file)
    
    # 篩選出台北市、新北市、基隆市和桃園市
    target_cities = ["臺北市", "新北市", "基隆市", "桃園市"]
    filtered_gdf = gdf[gdf['COUNTYNAME'].isin(target_cities)]
    
    return filtered_gdf

# 使用範例
if __name__ == "__main__":
    from cycu25305.ebus_taipei import taipei_route_info

    # 載入底圖
    try:
        base_map = load_base_map()
    except Exception as e:
        print(f"Error loading base map: {e}")
        sys.exit(1)

    # 初始化公車路線地圖
    bus_route_map = BusRouteMap(route_id='0161000900', direction="go", route_info_class=taipei_route_info)

    try:
        # 取得路線資料
        bus_route_map.fetch_route_data()
        # 建立幾何資料
        bus_route_map.create_geometry()
        # 繪製地圖，將公車路線疊加在底圖上
        bus_route_map.plot_route(base_map=base_map)
    except Exception as e:
        print(f"Error: {e}")