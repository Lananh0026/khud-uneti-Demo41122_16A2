list1=[74,74,72,72,73,69,69,71,76,71]
def chuyen_doi(x):
    cd=x*0.0254
    return cd
list_cd=list(map(chuyen_doi, list1))
print('List sau khi đổi từ inch sang mét:',list_cd)