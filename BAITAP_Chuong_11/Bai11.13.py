#1
set1=set()
a=int(input("Nhập giá trị cho set 1 :"))
print("Tiếp tục nhập giá trị?")
q=int(input("1 : có, 0 : không"))
while True:
    if q==1:
        a=int(input("Nhập giá trị cho set 1 :"))
        set1.add(a)
        print("Tiếp tục nhập giá trị?")
        q=int(input("1 : có, 0 : không"))
    if q==0:
        print("Set1 đã nhập xong!")
        break
set2=set()
e=int(input("Nhập giá trị cho set 2 :"))
print("Tiếp tục nhập giá trị?")
p=int(input("1 : có, 0 : không"))
while True:
    if p==1:
        e=int(input("Nhập giá trị cho set 2 :"))
        set2.add(e)
        print("Tiếp tục nhập giá trị?")
        p=int(input("1 : có, 0 : không"))
    if p==0:
        print("Set2 đã nhập xong!")
        break
print("Set1 :",set1)
print("Set2 :",set2)

#2
print("Set1 có",len(set1),"phần tử")
print("Set2 có",len(set2),"phần tử")

#3
print("Max set1 là :",max(set1))
print("Min set1 là :",min(set1))
print("Max set2 là :",max(set2))
print("Min set2 là :",min(set2))

#4
h = set1.pop()
print("pop set1 :",h)

#5 set union của set1 và set2
set3 =set1|set2
print("set 1 union set2 :",set3)

#6 set intersection của set1 và set2
set4=set1&set2
print("set 1 intersection set2 :",set4)

#7 set diference của set1 và set2
set5=set1-set2
print("set1 diference set2 :",set5)

#8 set symmetric difference của set1 và set2
set6=set1^set2
print("set1,set2 symmetric difference :",set6)

#sắp xếp set1 tăng dần và set2 giảm dần
print("set1 sắp xếp tăng dần :",sorted(set1))
print("set2 sắp xếp giảm dần :",sorted(set2 , reverse = True))