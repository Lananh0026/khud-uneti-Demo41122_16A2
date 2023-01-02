def Nhapso():
    while True:
        n = int(input('Chọn chức năng cần thực hiện(0-4): '))
        if (type(n) is not int) or (not 0<=n<=4):
             print('Yêu cầu không xác định.Yêu cầu nhập lại')
        else:
            return n
print('Bạn muốn làm gì?')
print('1.- Thêm liên hệ mới')
print('2.- Tìm tên')
print('3.- Xóa số , xóa tên')
print('4.- Xem danh bạ')
print('0.- Nhấn 0 để kết thúc ')
def main():
    dic = {'Tên ':'Số điện thoại','Bố': '0374064722','Mẹ': '0397011789','Em trai': '0986023572','Chúc': '0329507343','Lan': '036663204' }
    while True:
        choice = Nhapso()
        if choice==0:
            print('Mission Complete!!!')
            break
        elif choice==1:
            them_so(dic)
        elif choice==2:
            Tim_so(dic)
        elif choice==3:
            xoa_so(dic)
        elif choice==4:
            xem_danh_ba(dic)
def them_so(dic):
    print('\t1.- Thêm số')
    word = input('Tên : ')
    mean = input('Số điện thoại: ')
    dic[word] = mean
    print('Số mới đã được thêm: [%s : %s]'%(word,dic[word]))
def Tim_so(dic):
    print('\t2.- Tìm tên')
    word = input('Số điện thoại cần tìm: ')
    if word in dic:
        print('Danh bạ bạn cần tìm: [%s : %s]'%(word,dic[word]))
    else:
        print('Không tìm thấy tên %s trong danh bạ'%word)
def xoa_so(dic):
    print('\t3.- Xóa số:')
    word = input('Tên người cần xóa:')
    if word in dic:
        print('đã xóa danh bạ: [{0} : {1}]'.format(word,dic[word]))
        dic.pop(word)
    else:
        print('không tìm thấy danh bạ %s cần xóa'%word)
def xem_danh_ba(dic):
    print('\t4.- Xem danh bạ')
    if len(dic) == 0:
        print('Hiện tại danh bạ của bạn không có số nào.Bạn cần nhập thêm số mới')
    else:
        for i in dic:
            print(i,'  :  ' ,dic[i])
main()