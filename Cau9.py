def xac_dinh_quy(thang):
    if 1 <= thang <= 3:
        return "Quý 1"
    elif 4 <= thang <= 6:
        return "Quý 2"
    elif 7 <= thang <= 9:
        return "Quý 3"
    elif 10 <= thang <= 12:
        return "Quý 4"
    else:
        return "Tháng không hợp lệ"

# Test
print(xac_dinh_quy(9))  # Quý 3
print(xac_dinh_quy(12)) # Quý 4
a=int(input("Nhập tháng:"))
print(xac_dinh_quy(a))
