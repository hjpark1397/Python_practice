# * 하나는 가변 인수 ( 몇개든 인수를 받아들인다 )
def my_print(*contents):
    print(*contents)

my_print("hello")
my_print("hello", "world")
# packing 된 contents 인자를 다시 unpacking
# 여러 인수를 받는다

# 두개 **
# 가변 매개변수는 딕셔너리다
def asterisk_test(a, **kargs):
    print(a, kargs)
    print(type(kargs))

asterisk_test(1, b=2, c=3, d=4, e=5, f=6)
