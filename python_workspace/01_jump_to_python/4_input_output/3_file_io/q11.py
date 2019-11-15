# coding = UTF-8
def search_visitor(name):
    f = open('방명록.txt','r', encoding='UTF-8')
    list= f.readlines()
    f.close()
    for i in list:
        # i=i[:3]
        if name in i:
            return name
        else:
            pass
    return ''

def save(name):
    f = open('방명록.txt','a', encoding='UTF-8')
    f.write("\n"+(name)+(' ')+input("생년월일을 입력하세요.(예:801212): "))
    f.close()

while True:
    name = input("이름을 입력하세요: ")
    a =  search_visitor(name)
    if name == a:
        print(f"{name}님 다시 방문해 주셔서 감사합니다. 즐거운 시간되세요")
    else:
        save(name)
    break
