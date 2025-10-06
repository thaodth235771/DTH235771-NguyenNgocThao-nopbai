i=int(input("Nhap i:"))
j=int(input("Nhap j:"))
k=int(input("Nhap k:"))
if i<j:
    if j<k:
        i=j
    else:
        j=k
else:
    if j>k:
        j=i
    else:
        i=k
print("i=",i,"j=",j,"k=",k)


