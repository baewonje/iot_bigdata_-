#coding=cp949

prompt="""
1. 입력
2. 종료
    입력: """
ingredint_list=[]

def input_ingredint():
    while True:
        input_list=input("안녕하세요. 원하시는 재료를 넣어주세요.: ")
        if input_list == '종료':
            return
        else:
            ingredint_list[:] += [input_list]

def make_sandwiches():
    print("샌드위치를 만듭니다.")
    for i in ingredint_list[:]:
        print(f"{i}  추가합니다.")
    print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")

while True:
    choice = int(input(prompt))
    if choice == 1:
        input_ingredint()
        make_sandwiches()
        break
    elif choice == 2:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 번호를 입력하셨습니다.")
        continue

