def asterisk_test_2(*args):
    x, y, *z = args #언패킹~
    return x,y,z

print(asterisk_test_2(3,4,5,10,20))