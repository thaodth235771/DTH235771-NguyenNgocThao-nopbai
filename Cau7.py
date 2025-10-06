from datetime import datetime, timedelta

def ngay_ke_tiep(ngay, thang, nam):
    try:
        current_date = datetime(nam, thang, ngay)
        next_day = current_date + timedelta(days=1)
        return next_day.strftime("%d/%m/%Y")
    except ValueError:
        return "Ngày không hợp lệ"

# Test
print(ngay_ke_tiep(21, 9, 2025))  # 22/09/2025
print(ngay_ke_tiep(31, 12, 2024)) # 01/01/2025
d=int(input("Nhap ngay:"))
m=int(input("Nhap thang:"))
y=int(input("Nhap nam:"))
print(ngay_ke_tiep(d,m,y))
