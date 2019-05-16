#일반적인 함수 사용
def f(x, y):
    return x+y

print(f(1, 4))

#람다 함수 사용
f=lambda x, y : x + y #앞쪽 x, y는 매개변수의 이름이다. 뒤는 매개변수가 반환하는 결과 값
print(f(1, 4))
#람다 함수는 별도의 def나 return을 작성하지 않는다.

print((lambda x:x+1)(5)) #6으로 출력된다.
#어떤 변수에 람다 함수를 할당하여 함수와 비슷한 형태로 사용한다.
#괄호에 람다 함수를 넣고, 인수(argument)로 5 입력.

#람다 함수의 다양한 형태
f = lambda x, y: x + y
print(f(1, 4))

f = lambda x: x**2
print(f(3))

f = lambda x: x/2
print(f(3))
#print(f(3, 5)) = 매개변수의 개수를 넘어가는 인수가 입력되면 오류가 발생한다.
