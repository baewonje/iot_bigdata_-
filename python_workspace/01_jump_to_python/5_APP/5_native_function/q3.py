import random

lotto_list = []

for i in range(6):
    number= random.randint(1,45)
    if number not in lotto_list :
        lotto_list.append(number)

print(lotto_list)