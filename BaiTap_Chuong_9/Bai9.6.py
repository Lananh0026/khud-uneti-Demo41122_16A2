n=int(input('Nhập vào số nguyên dương:'))
dem=0
for i in range(1,n+1):
    if n % i ==0:
        dem+=1
if dem==2:
        print(n,'Là số nguyên tố')
        print(True)        
else:
        print('Không là số nguyên tố',n)
        print(False)
   
