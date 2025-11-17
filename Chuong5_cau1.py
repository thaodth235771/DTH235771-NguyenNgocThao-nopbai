def CheckDoiXung(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True
def main():
    s = input("Nhập 1 chuỗi: ")
    if CheckDoiXung(s):
        print("Chuỗi bạn nhập đối xứng")
    else:
        print("Chuỗi bạn nhập không đối xứng")
while True:
    main()
    choice = input("Tiếp không bạn? (c/k): ").lower()
    if choice == "k":
        break

print("CÁM ƠN BẠN")