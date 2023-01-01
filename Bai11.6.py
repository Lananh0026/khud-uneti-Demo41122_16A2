list1=[74,74,72,72,73,69,69,71,76,71]
def chuyen_doi(x):
    cd=x*0.0254
    return cd
list_cd=list(map(chuyen_doi, list1))
print('List sau khi đổi từ inch sang mét:',list_cd)
#in ra 3 chiều cao đầu tiên và 3 chiều cao cuối cùng
print('3 chiều cao đầu tiên là:',list_cd[0:3])
print('3 chiều cao cuối cùng là:',list_cd[6:9])
#Chiều cao trung bình, chiều cao lớn nhất, chiều cao nhỏ nhất
tb=sum(list_cd)/len(list_cd)
print('Chiều cao trung bình là:',tb)
print('Chiều cao lớn nhất là:',max(list_cd))
print('Chiều cao nhỏ nhất là:',min(list_cd))
#Sắp xếp tăng dần
list_cd.sort()
print('Chiều cao tăng dần là:',list_cd)
#Sắp xếp giảm dần
list_cd.sort()
list.reverse()
print('Chiều cao sắp xếp giảm dần là:',list_cd)
