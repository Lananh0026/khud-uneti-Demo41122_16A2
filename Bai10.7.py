chuoi=input('Mời bạn nhập chuỗi:')
print('Chuỗi bạn nhập=',chuoi)
print(chuoi,len(chuoi))
chuoi1=chuoi.strip()
print(chuoi1,len(chuoi1))
print(chuoi.title())
#chưa bt lm ý 3
c=chuoi.count('s_sub')
print('s_sub xuất hiện=',c)
#ý 4
x=chuoi.find('s_find')
print(x)
x1=chuoi.rfind('s_replace')
print(x1)