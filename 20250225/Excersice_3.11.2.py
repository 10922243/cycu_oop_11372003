def print_right(text):
    width = 40  # 設定右對齊的寬度
    padding = width - len(text)  # 計算需要填充的空格數量
    print(' ' * padding + text)  # 使用空格填充並連接字串

print_right("Monty")
print_right("Python's")
print_right("Flying Circus")