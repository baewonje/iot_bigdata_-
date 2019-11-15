f1 = open("test1.txt", 'w')
f1.write("life is too short1")

f1.close()

f2 = open("test1.txt", 'r',encoding='UTF-8')
print (f2.read(),end='')

f2.close()