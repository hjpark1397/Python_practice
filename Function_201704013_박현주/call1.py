def f(x):
    y=x
    x=5
    return y*y

x=3
print(f(x)) #위의 x=3이 함수에 전달되어 y=3이 되고 결과가 9가 나온다
print(x)#x=3