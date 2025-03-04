# 寫出一個函數 輸入 為兩個整數 , 輸出為兩個整數的最大公因數
# 輾轉相除法
# 使用 遞迴 完成!

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
a = int(input())
b = int(input())
print(gcd(a, b))

# 這個方法是最快的
# 但是如果要求最小公倍數的話
# 可以用 a * b / gcd(a, b) 來求得
# 這樣就可以得到最小公倍數了

#測試範例
# 11 121
a, b = 11, 121
print(gcd(a, b)) # 11
# 7 49
a, b = 7, 49
print(gcd(a, b)) # 7