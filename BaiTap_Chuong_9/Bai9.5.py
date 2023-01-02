def Tinh_gia_tri(n,x):
    return ((x*x+x+1)**n)+(x*x-x+1)**n
print('Nhập vào x:')
x=int(input())
print('Nhập vò n:')
n=int(input())  
A=Tinh_gia_tri(n,x) 
print('A=',A) 