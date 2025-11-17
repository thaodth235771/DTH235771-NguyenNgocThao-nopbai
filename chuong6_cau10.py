# Hàm tạo ma trận từ nhập liệu
def input_matrix(m, n, name="Matrix"):
    print(f"Nhập các phần tử của {name}:")
    M = []
    for i in range(m):
        row = list(map(int, input(f"Dòng {i+1}: ").split()))
        if len(row) != n:
            print(f"Phải nhập đúng {n} phần tử!")
            return input_matrix(m, n, name)
        M.append(row)
    return M

# Hàm in ma trận
def print_matrix(M):
    for row in M:
        print("\t".join(map(str,row)))
    print()

# Hàm cộng 2 ma trận
def add_matrix(A,B):
    m = len(A)
    n = len(A[0])
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

# Hàm tính ma trận hoán vị
def transpose(M):
    m = len(M)
    n = len(M[0])
    T = []
    for j in range(n):
        row = []
        for i in range(m):
            row.append(M[i][j])
        T.append(row)
    return T

# Nhập ma trận
m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

A = input_matrix(m,n,"Matrix A")
B = input_matrix(m,n,"Matrix B")

print("Matrix A:")
print_matrix(A)
print("Matrix B:")
print_matrix(B)

# Cộng ma trận
C = add_matrix(A,B)
print("Matrix A + B:")
print_matrix(C)

# Hoán vị
print("Hoán vị của Matrix A:")
print_matrix(transpose(A))
print("Hoán vị của Matrix B:")
print_matrix(transpose(B))
