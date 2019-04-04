def f():
    global s #전역변수 사용 키워드
    s="I love London!"
    print(s)

s="I love Paris!"
f()
print(s)