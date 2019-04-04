def calculate(x, y):
    total=x+y #새로운 값이 할당되어 함수 안 total은 지역 변수가 됨
    print("In Function")
    print("a:", str(a), "b:", str(b), "a+b", str(a+b), "total:", str(total))
    return total

a=5
b=7 #a와 b는 전역변수
total=0 #전역변수 total
print("In Program-1")
print("a:", str(a), "b:", str(b), "a+b", str(a+b))

sum = calculate(a, b)
print("After Calculation")
print("Total:", str(total), "Sum:", str(sum)) #지역변수는 전역변수에 영향을 주지 않는다.
