def Nhapso():
    while True:
        n = int(input('Chọn chức năng cần thực hiện(0-4): '))
        if (type(n) is not int) or (not 0<=n<=4):
             print('Yêu cầu không xác định.Yêu cầu nhập lại')
        else:
            return n
print('Bạn muốn làm gì?')
print('1.- Thêm từ')
print('2.- Tìm từ')
print('3.- Xóa từ')
print('4.- Xem từ điển')
print('0.- Nhấn 0 để kết thúc ')
def main():
    dic = {'cat':'con mèo','dog':'con chó','ant':'con kiến',}
    while True:
        choice = Nhapso()
        if choice==0:
            print('Mission Complete!!!')
            break
        elif choice==1:
            them_tu(dic)
        elif choice==2:
            Tim_tu(dic)
        elif choice==3:
            xoa_tu(dic)
        elif choice==4:
            xem_tu_dien(dic)
def them_tu(dic):
    print('\t1.- Thêm từ')
    word = input('Từ mới: ')
    mean = input('Nghĩa tiếng việt: ')
    dic[word] = mean
    print('Từ mới đã được thêm: [%s : %s]'%(word,dic[word]))
def Tim_tu(dic):
    print('\t2.- Tìm từ')
    word = input('từ cần tìm: ')
    if word in dic:
        print('Từ bạn cần tìm: [%s : %s]'%(word,dic[word]))
    else:
        print('Không tìm thấy từ %s trong từ điển'%word)
def xoa_tu(dic):
    print('\t3.- Xóa từ:')
    word = input('từ cần xóa:')
    if word in dic:
        print('đã xóa từ: [{0} : {1}]'.format(word,dic[word]))
        dic.pop(word)
    else:
        print('không tìm thấy từ %s cần xóa'%word)
def xem_tu_dien(dic):
    print('\t4.- Xem từ điển')
    if len(dic) == 0:
        print('Hiện tại từ điển của bạn không có từ nào.Bạn cần nhập thêm từ mới')
    else:
        for i in dic:
            print(i,'  :  ' ,dic[i])
main()

