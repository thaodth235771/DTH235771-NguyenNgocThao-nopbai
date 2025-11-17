n = int(input("Nhập số lượng phần tử: "))

lst = []

print("Nhập các số theo thứ tự tăng:")

for i in range(n):
    while True:
        x = int(input(f"Nhập số thứ {i+1}: "))
        
        # nếu đây không phải số đầu tiên thì phải so sánh với phần tử trước
        if i == 0 or x >= lst[i-1]:
            lst.append(x)
            break
        else:
            print("Sai quy cách! Số mới phải >= số trước. Nhập lại!")

print("Dãy số sau khi nhập xong:")
print(lst)
