def asterisk_test(a, b, *args):
    return a+b+sum(args)

print(asterisk_test(1, 2, 3, 4, 5)) #1,2는 제대로 들어가고 나머지들은 전부다 args에 넣어주는것임 (*args가 가변인수)