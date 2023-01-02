from datetime import datetime
a=int(input('Nhập ngày:'))
b=int(input('Nhập tháng:'))
c=int(input('Nhập năm:'))
print('Ngày tháng năm vừa nhập:',a,'-',b,'-',c)
if (c % 4 ==0 and c % 100 !=0) or c % 400 ==0:
    print('Năm',c,'là năm nhuận')
else:
    print('Năm',c,'không nhuận')

