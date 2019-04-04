def test(t):
    print(x)
    t=20 #지역변수
    print("In Function:", t)

x=10 #전역 변수
test(x)
print("In Main:", x)
print("In Main:", t)