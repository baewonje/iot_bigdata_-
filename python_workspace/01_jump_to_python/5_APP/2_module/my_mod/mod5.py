def my_add (a,b):
    return a+b
def my_sub(a,b):
    return a-b

# 아래와 같이 테스트 코드로서 동작하기 위한 용도로
# 조건을 체크하는 코드를 'boilerplate code'라고 한다.
if __name__=="__main__":
    print(my_add(5,4))
