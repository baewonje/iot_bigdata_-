#coding = UTF-8
def show_candidates(candidate_list):
    for i in candidate_list:
        print(f"{i}",end='')
def make_idol(candidate_list):
    for i in candidate_list:
        i=i.rstrip("\n")
        print("신예 아이돌 "+i+"인기 급상승")
def make_world_star(candidate_list):
    for i in candidate_list:
        i=i.rstrip("\n")
        print("아이돌"+f"{i}"+"월드스타 등극")

f = open("연습생.txt",'r',encoding='UTF-8')

while True:
    candidate_list = f.readlines()
    show_candidates(candidate_list)
    print("\n")
    make_idol(candidate_list)
    print("\n")
    make_world_star(candidate_list)
    break
f.close()

