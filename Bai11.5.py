list=[]
while True: 
        a=int(input('Nhập giá trị:'))
        hoi=input('(Tiếp tục nhập giá trị?(1/0:)')
        list.insert(0,a)
        if hoi=='0':
            list.reverse()
            print('List:',list) 
            break
#Ktra số nguyên tố
def ktrasont(n):
    dem=0
    for i in range(1,n+1):
        if n%i ==0:
            dem+=1
    return dem==2
demnt=0
m=[]
for x in list:
    if ktrasont(x):
        demnt+=1
        m.append(x)
print('Có',demnt,'sô nguyên tố trong list',m)   
#Các phần tử âm
n=[]
for x in list:
    if x< 0:
        n.append(x)
print('Các phần tử âm trong list:',n)
g=sum(n)/len(n)
print('Trung bình cộng các phần tử âm:', round(g,2))
#Các phần tử dương
d=[]
for x in list:
    if x> 0:
        d.append(x)
print('Các phần tử âm trong list:',d)
h=sum(d)/len(d)
print('Trung bình cộng các phần tử âm:', round(h,2))
#Max,min
print('Gía trị max trong list:',max(list))
print('Gía trị min trong list:',min(list))
#Sắp xếp list tăng dần
list.sort()
print('List sắp tăng dần',list)
