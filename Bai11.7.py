L=[1,2,3,4]
thresh=2
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