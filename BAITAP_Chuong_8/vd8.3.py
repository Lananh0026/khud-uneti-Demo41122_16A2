# xét kết quả học tập
diem_TB = eval(input("Nhập điểm trung bình="))
if diem_TB >=0 and diem_TB <=10:
    if diem_TB <5:
       print("loại yếu kém!")
    elif diem_TB <6:
       print("xếp loại trung bình")
    elif diem_TB <7:
        print("Trung bình-khá!")
    elif diem_TB <8:
        print("Khá!!")
    elif diem_TB <9:
         print("Gioi!!")
    else:
        print("Xuất sắc!!")
else:
    print("Điểm nhập vào không hợp lệ!")               


     