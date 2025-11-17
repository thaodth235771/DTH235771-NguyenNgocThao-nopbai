# Dữ liệu mẫu
M = [3,6,7,8,11,17,2,90,2,5,4,5,8]

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Tách số lẻ, chẵn, nguyên tố, không nguyên tố
odd = [x for x in M if x % 2 == 1]
even = [x for x in M if x % 2 == 0]
primes = [x for x in M if is_prime(x)]
non_primes = [x for x in M if not is_prime(x)]

# Xuất kết quả
print("Số lẻ:", odd, "Tổng số lẻ =", len(odd))
print("Số chẵn:", even, "Tổng số chẵn =", len(even))
print("Số nguyên tố:", primes)
print("Số không phải nguyên tố:", non_primes)
