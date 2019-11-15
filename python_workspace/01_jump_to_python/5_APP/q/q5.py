list = [0,1]
min = 0
max = 1

number = int(input("입력 : "))
while True:
    if number >=list[min]+list[max]:
        list.append(list[min]+list[max])
        min +=1
        max +=1
    else:
        break
print(list)
