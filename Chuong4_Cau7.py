import math

# Nhập tọa độ điểm A
xA = float(input("Nhập xA: "))
yA = float(input("Nhập yA: "))

# Nhập tọa độ điểm B
xB = float(input("Nhập xB: "))
yB = float(input("Nhập yB: "))

# Tính độ dài đoạn AB
AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)

# Xuất kết quả
print(f"Độ dài đoạn AB là: {AB}")
