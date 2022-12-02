def BMI(height,weight):
    return weight/(height**2)
def Phanloai(bmi):
    if bmi<18.5:
        return"Gầy"
    elif bmi<=24.9:
        return"Bình thường"
    elif bmi<=29.9:
        return"Hơi béo"
    elif bmi<=34.9:
        return"Béo phì cấp độ 1"
    elif bmi<=39.9:
        return"Béo phì cấp độ 2"
    else:
        return"Béo phì cấp độ 2"
print('Nhập vào chiều cao:')
height=float(input())
print('Nhập cào cân nặng')
weight=float(input())
bmi=BMI(height,weight)
print('BMI của bạn=',bmi)
print('Phân loại của bạn=',Phanloai(bmi))                

            