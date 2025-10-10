import math

n = int(input("Nhập số lượng dấu căn (n): "))

# Nhập các hệ số a_i
a = 2
'''for i in range(n):
    val = float(input(f"Nhập a_{i+1}: "))
    a.append(val)'''

# Tính căn bậc 2 lồng nhau từ dưới lên
result = 0
for i in range(n-1, -1, -1):
    result = math.sqrt(a + result)

print(f"Kết quả căn bậc 2 lồng nhau là: {result}")
