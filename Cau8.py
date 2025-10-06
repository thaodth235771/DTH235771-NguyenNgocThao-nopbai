def tinhtoan(a,b,toantu):
    try:
        if toantu=="+":
            return a+b
        elif toantu=="-":
            return a-b
        elif toantu == "*":
            return a * b
        elif toantu == "/":
            if b==0:
                return"Không chia được cho 0!"
            return a / b
        else:
            return "Phép toán không hợp lệ"
    except:
        return "Lỗi tính toán"
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
c=str(input("Nhập toán tử:"))
print(tinhtoan(a,b,c))

