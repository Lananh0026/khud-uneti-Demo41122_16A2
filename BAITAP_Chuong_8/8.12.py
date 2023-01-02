#Kiểm tra một số nhập từ bàn phím có phải là nguyên tố không
n = int(input("Nhập số n ="))
flag = True      #Kỹ thuật lính canh
if n<2:
    print(n, "Không nguyên tố!!!")
else:
    for i in range(2, int(n/2)):
        if n%i == 0:
            flag = False
            break
    if flag :
        print(n, "Là số nguyên tố")
    else:
        print(n, "Không phải là số nguyên tố!!!")