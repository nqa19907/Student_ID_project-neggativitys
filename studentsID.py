def menu():
    print('''
================ Classroom Data Manager ================
                Chọn thao tác thực hiện:
0. Menu
1. Thêm học sinh
2. Hiển thị tất cả điểm
3. Tìm điểm theo tên học sinh
4. Thoát
''')
class classroom:
    def __init__(self):
        self.students=[]
    def add(self):
        a,b,c=map(str,input().split())
        dic={'id':a,'name':b,'score':c}
        self.students+=[dic]
        return ''
    def display(self):
        for key in self.students:
            print(f'id:{key['id']}, name:{key['name']}, score:{key['score']}')
        return ''
    def search_by_name(self,s):
        for i in self.students:
            if i['name']==s:
                return i['score']
        return 'sinh vien khong ton tai'
    def search_by_id(self,m):
        for i in self.students:
            if i['id']==m:
                return i['score']
        return 'sinh vien khong ton tai'
s1=classroom()
print('''
================ Classroom Data Manager ================
                Chọn thao tác thực hiện:
0. Menu
1. Thêm sinh viên
2. Hiển thị tất cả điểm
3. Tìm điểm theo tên sinh viên
4. Tìm điểm theo mã sinh viên
5. Thoát
''')
while True:
    choice=input()
    if choice=='0':
        menu()    
    if choice=='1':
        print(s1.add())
    elif choice=='2':
        print(s1.display())
    elif choice=='3':
        m=input()
        print(s1.search_by_name(m))
    elif choice=='5':
        break
    elif choice=='4':
        m=input()
        print(s1.search_by_id(m))




