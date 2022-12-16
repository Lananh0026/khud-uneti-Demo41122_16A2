from random import randrange


n=int(input('Nhập số phần tử:'))
L=[0]*n
for i in range(n):
    L[i]=randrange(-100,100)
thresh=int(input('Nhập thresh:'))
print(L)
m=[]
n=[]
for i in range(len(L)):
        x=L[i]
        if thresh>i:
            m.append('False')
        else:
           n.append('True') 
a=m+n
print(a)
