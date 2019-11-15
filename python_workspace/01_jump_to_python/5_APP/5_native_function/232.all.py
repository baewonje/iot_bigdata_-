# all은 iterable 객체 (2개 이상의 값을 담을 수 있는 자료형)에 적용가능하다.
# all 함수는 입력받은 데이터의 정합성을 체크할 때 사용할 수 있다.
print(all([1,2,3]))          # 숫자형
print(all([1,2,0]))
print(all(['hello','world'])) #  문자열
print(all(['hello','']))
print(all(['hello',' ']))
print(all((1,2)))               # 튜플
print(all((1,0)))
print(all(list({}.values())))
# dictionary의 값은 key. value 로 나뉘어 확인
print(all({'조문수':'남','김혜경':'여'})) # dictionary
print(all({}))                            # dictionary
print(all([1,2,'3',0,0]))                 # 복합 자료형

result = [1,2,3].append(4) # 상수형 객체에 값을 변경하는 멤버함수사용은 주의
print(result)

result = [1,2,3]
result.append(4)
print(result)

print([1,2,3].count(2)) # 상수형 객체의 값을 조회 하는 멤버함수는 가능