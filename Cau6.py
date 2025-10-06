def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi",
                 "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    if n < 0 or n > 99:
        return "Số không hợp lệ"
    elif n < 10:
        return don_vi[n].capitalize()
    else:
        chuc = n // 10
        dv = n % 10
        if dv == 0:
            return hang_chuc[chuc].capitalize()
        elif dv == 1 and chuc > 1:
            return f"{hang_chuc[chuc]} mốt".capitalize()
        elif dv == 5 and chuc > 0:
            return f"{hang_chuc[chuc]} lăm".capitalize()
        else:
            return f"{hang_chuc[chuc]} {don_vi[dv]}".capitalize()

# Test
print(doc_so(35))  # Ba mươi lăm
print(doc_so(5))   # Năm
n=int(input("Nhap n:"))
print(doc_so(n))
