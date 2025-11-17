import re

def NegativeNumberInStrings(s):
    negatives = re.findall(r'-\d+', s)
    return negatives

s = input("Nhập chuỗi: ")
print("Các số nguyên âm trong chuỗi là:", NegativeNumberInStrings(s))
