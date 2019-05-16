#map( )함수의 사용
ex = [1, 2, 3, 4, 5]
f = lambda x: x ** 2
print(list(map(f, ex)))
# 결과 [1, 4, 9, 16, 25]
# ex라는 이름의 리스트 형성
# 입력된 값을 제곱하는 람다 함수 f 생성
# map(함수 이름, 리스트 데이터)의 구조
# 해당 코드로 함수 f를 ex의 각 요소에 맵핑하라!

#리스트를 안붙이고 하는 방법도 있음!
ex = [1, 2, 3, 4, 5]
f = lambda x: x**2
for value in map(f, ex):
    print(value)

#한줄씩 출력해줌!

#리스트 컴프리헨션으로 충분히 해낼 수 있다!
ex = [1, 2, 3, 4, 5]
[x ** 2 for x in ex]
print([x ** 2 for x in ex])
#같은 결과가 나온다!

#map( )함수의 시퀀스 자료형 데이터 처리
ex =[1, 2, 3, 4, 5]
f = lambda x, y: x+y
print(list(map(f, ex, ex)))

#리스트 컴프리헨션으로 변경
[x+y for x, y in zip(ex, ex)]
print([x+y for x, y in zip(ex, ex)])

# 위 아래는 같은 결과이다.
# ex 변수와 같은 위치에 있는 값끼리 더한 결과 출력

#짝수일 때는 각 수를 제곱하고, 그렇지 않을 때는 해당 수를 출력
list(map(lambda x: x ** 2 if x % 2 == 0 else x, ex)) #map( ) 함수
# [1, 4, 3, 16, 5]

[x ** 2 if x % 2 == 0 else x for x in ex] #리스트 컴프리헨션
# [1, 4, 3, 16, 5]

#리스트 컴프리헨션이 조금 더 직관적

#reduce( ) 함수
from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
# 15
# x 는 기존의 x + y를 적용한 값을 계속 저장하는 변수
# 뒤의 y는 리스트에 있는 값을 하나씩 할당받는 변수
# 값을 차례대로 뽑는다는 것 = 기존 map( ) 함수와 같음
# 리스트 변수의 모든 값을 람다 함수로 모두 적용한다는 차이점

#일반 for문
x = 0
for y in [1, 2, 3, 4, 5]:
    x += y

print(x)
# 15