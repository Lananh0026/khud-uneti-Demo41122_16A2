n=int(input('Nhập n:'))
s=0
for i in range(1,n+1):
   if(i% 2==0):
     schan+=i
   else:
     sle+=i
print('A=',schan)    
print('B=',sle)
