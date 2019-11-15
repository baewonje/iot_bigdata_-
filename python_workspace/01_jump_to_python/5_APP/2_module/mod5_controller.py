# import mod2
# print(mod2.my_add(3,4))
# print(mod2.my_sub(3,4))
# 파일명에 controller가 들어가면 전체 프로그램을 제어하는
#  역할을 수행함을 의미한다.
# 따라서 많은 외부, 내부 모듈을 아래와 같이 사용하게 된다.

# from ./my_mod/mod5 import *    # 모듈은 왼쪽 코드와 같이 상대경로가 불가능하다.
import sys
# 개발 중에는 모듈 경로를 파이참에 추가하고
#  배포시에는 경로를 코드상에 추가한다.
# sys.path.append("C:\\python_workspace\\01_jump_to_python\\5_APP\\2_module\\my_mod")
# sys.path.append('.\\my_mod')
# sys.path.append('./my_mod')
sys.path.append('my_mod')
from mod5 import *

print("mod5 controller ver1 initializing..")
input("초기화가 완료되었습니다. 구동하시겠습니까?")

num1 = int(input("첫번째 수를 입력하세요: "))
num2 = int(input("두번째 수를 입력하세요: "))

print("자! 그럼 입력받은 두 수에 대한 덧셈과 뺄셈의 결과를 보여드리겠습니다. ")
print(my_add(num1,num2))
print(my_sub(num1,num2))
