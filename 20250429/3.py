stations = [
    ["進站中", "001", "站牌A", "ID001", 25.0330, 121.5654],
    ["5分鐘", "002", "站牌B", "ID002", 25.0340, 121.5664],
    ["10分鐘", "003", "站牌C", "ID003", 25.0350, 121.5674],
]

route_id = "0100022500"

def draw_map(stations, route_id):
    # Placeholder implementation for draw_map
    print(f"Drawing map for route {route_id} with stations:")
    for station in stations:
        print(f"Station {station[2]} at coordinates ({station[4]}, {station[5]})")

draw_map(stations, route_id)