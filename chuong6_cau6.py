from random import sample

n = int(input("Nhập số phần tử N: "))

# sinh danh sách gồm n số ngẫu nhiên từ -100 đến 100, không trùng nhau
lst = sample(range(-100, 101), n)

print("List ngẫu nhiên không trùng nhau là:")
print(lst)
