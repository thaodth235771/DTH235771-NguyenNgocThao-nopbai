def optimize_name(s):
    # Xóa khoảng trắng dư, tách từ
    words = s.strip().split()

    # Viết hoa chữ cái đầu mỗi từ
    words = [word.capitalize() for word in words]

    # Ghép lại
    return " ".join(words)

s = input("Nhập chuỗi danh từ: ")
print("Chuỗi tối ưu:", optimize_name(s))
