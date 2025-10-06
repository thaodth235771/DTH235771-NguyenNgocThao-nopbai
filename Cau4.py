'''Cho x, y, z = 3, 5, 7. Hãy cho biết kết quả của Boolean Expression
(a) x == 3
(b) x < y
(c) x >= y
(d) x <= y
(e) x != y - 2
(f) x < 10
(g) x >= 0 and x < 10
(h) x < 0 and x < 10
(i) x >= 0 and x < 2
(j) x < 0 or x < 10
(k) x > 0 or x < 10
(l) x < 0 or x > 10'''
x,y,z=3,5,7
#(a)
if x==3:
    print("True")
else:
    print("False")
#(b)
if x<y:
    print("True")
else:
    print("False")
#(c)
if x>=y:
    print("True")
else:
    print("False")
#(d)
if x<=y:
    print("True")
else:
    print("False")
#(e)
if x!=y-2:
    print("True")
else:
    print("False")
#(g)
if x<=0&x<10:
    print("True")
else:
    print("False")
#(h)
if x<0&x<10:
    print("True")
else:
    print("False")
#(i)
if 0<=x<2:
    print("True")
else:
    print("False")
#(j)
if x<0 or x<10:
    print("True")
else:
    print("False")
#(k)
if x>0 or x<10:
    print("True")
else:
    print("False")
#(l)
if x<0 or x>10:
    print("True")
else:
    print("False")