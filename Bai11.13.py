def BMI(height,weight):
    return weight/(height**2)
def Phanloai(bmi):
    if bmi<18.5:
        return"Gầy"
    elif bmi<=24.99:
        return"Bình thường"
    else:
        return"Thừa cân"
print('Nhập vào chiều cao:')
height=float(input())
print('Nhập cào cân nặng')
weight=float(input())
bmi=BMI(height,weight)
print('BMI của bạn=',bmi)
print('Phân loại của bạn=',Phanloai(bmi))  