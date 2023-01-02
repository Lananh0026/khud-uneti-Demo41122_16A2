#8.7
x=int(input("Nhập số Kwh: "))
if 0<=x<=50:
    print("tổng số tiền là: ",x*1678,"đồng")
elif 51<=x<=100:
    print("tổng số tiền là: ",x*1734,"đồng")
elif 101<=x<=200:
    print("tổng số tiền là: ",x*2014,"đồng")
elif 201<=x<=300:
    print("tổng số tiền là: ",x*2536,"đồng")
elif 301<=x<=400:
    print("tổng số tiền là: ",x*2834,"đồng")
elif x>=400:
    print("tổng số tiền là: ",x*2927,"đồng")

