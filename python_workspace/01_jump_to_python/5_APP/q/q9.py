f = open("sample.txt",'r')
list = f.readlines()
f.close()
total = 0

for i in list:
    total = total + int(i)

average = total/len(list)

print(average)
print(total)

f = open("result.txt",'w')
f.write(str(average))
f.close()