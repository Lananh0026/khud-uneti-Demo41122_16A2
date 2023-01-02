list=[]
while True: 
        a=int(input('Nhập giá trị:'))
        hoi=input('(Tiếp tục nhập giá trị?(1/0:)')
        list.insert(0,a)
        if hoi=='0':
            list.reverse()
            print('List:',list) 
            break
y=int(input('Nhập số cần tìm:'))
#Tổng các phần tử list
print('Tổng các phần tử trong list:',sum(list))
#Đếm 
z=list.count(y)
print(y,'Xuất hiện',z,'lần trong list')
#số nhỏ hơn y
list.insert(0,y)
   
