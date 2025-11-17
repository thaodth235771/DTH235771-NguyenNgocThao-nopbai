def analyze_string(s):
    vowels = "aeiouAEIOU"
    
    upper_count = 0
    lower_count = 0
    digit_count = 0
    special_count = 0
    space_count = 0
    vowel_count = 0
    consonant_count = 0

    for ch in s:
        if ch.isupper():
            upper_count += 1
        elif ch.islower():
            lower_count += 1

        if ch.isdigit():
            digit_count += 1

        if ch.isspace():
            space_count += 1

        if not ch.isalnum() and not ch.isspace():
            special_count += 1

        if ch.isalpha():
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    print("Số chữ IN HOA:", upper_count)
    print("Số chữ in thường:", lower_count)
    print("Số chữ số:", digit_count)
    print("Ký tự đặc biệt:", special_count)
    print("Khoảng trắng:", space_count)
    print("Nguyên âm:", vowel_count)
    print("Phụ âm:", consonant_count)


s = input("Nhập chuỗi: ")
analyze_string(s)
