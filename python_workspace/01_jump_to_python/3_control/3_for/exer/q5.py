#coding=cp949

total = 0
m = []
n = []
p = []


m = int(input("총 건수(m): "))
n = int(input("게시물 수(n): "))

print('m','n','출력')
while True:
    p = m/n+1
    if m>=n:
        print("%d %d %d"%(m,n,p))
    print(p)



