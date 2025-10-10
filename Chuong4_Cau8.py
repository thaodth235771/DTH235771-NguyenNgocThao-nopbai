import math

# Nhập cơ số a
a = float(input("Nhập cơ số a (a > 0 và a != 1): "))
# Nhập số x
x = float(input("Nhập số x (x > 0): "))

# Kiểm tra điều kiện đầu vào
if a <= 0 or a == 1:
    print("Sai điều kiện: a phải lớn hơn 0 và khác 1.")
elif x <= 0:
    print("Sai điều kiện: x phải lớn hơn 0.")
else:
    # Tính log_a x = ln(x) / ln(a)
    result = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {result}")
