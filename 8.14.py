a = int(input("Nhập số nguyên N:"))
b = 0
for i in range(1,a+1):
    print("Nhập số hạng thứ:",i)
    b1=int(input())
    b= b + b1
print("Tổng",a,"số hạng là",b)    