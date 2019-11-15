a= [20,55,67,82,45,33,90,87,100,25]
count = 0
total = 0
for i in a:
    if i >= 50:
        count +=1
        total += i

print(total/count)
