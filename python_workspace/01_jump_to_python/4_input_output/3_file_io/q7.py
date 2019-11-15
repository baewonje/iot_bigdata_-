f = open('test.txt','r',encoding='UTF-8')
body = f.read()
f.close()

body= body.replace("java","python")

f= open('test.txt','w',encoding='UTF-8')
f.write(body)
f.close()


f2 = open("test.txt", 'r',encoding='UTF-8')
print (f2.read(),end='')

f2.close()