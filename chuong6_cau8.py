n = int(input("Nhập số phần tử n: "))

M = []

# Nhập dãy số thực
for i in range(n):
    x = float(input(f"M[{i}] = "))
    M.append(x)

# Sắp xếp giảm dần
M.sort(reverse=True)

print("Dãy số sau khi sắp xếp giảm dần:")
print(M)
