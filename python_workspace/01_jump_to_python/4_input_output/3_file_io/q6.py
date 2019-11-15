user_input = input("저장할 내용을 입력하세요: ")
f = open('test.txt','a',encoding='UTF-8')
f.write(user_input)
f.write("\n")
f.close()

f2 = open("test.txt", 'r',encoding='UTF-8')
print (f2.read(),end='')

f2.close()