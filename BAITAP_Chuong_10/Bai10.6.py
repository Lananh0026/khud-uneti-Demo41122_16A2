from math import sqrt
a=float(input('Nhập a:'))
b=float(input('Nhập b:'))
c=float(input("Nhập c:"))
if a==0:
    if b==0 and c==0:
        print('vố số nghiệm')
    elif b==0 and c !=0:
        print('Vô nghiệm')
    else:
        x=-b/a
        print('Nghiệm x=',x)
else:
    delta=b**2-4*a*c
if delat<0:
        print('Vô nghiệm')
elif delat==0:
        x=-b/(2*a)
        print('Nghiệm kép x1=x2=',x)
else:
        x1=(-b-sqrt(delat))/(2*a)      
        x2=(-b+sqrt(delat))/(2*a)    
        print('x1=',x1)
        print('x2='.x2)