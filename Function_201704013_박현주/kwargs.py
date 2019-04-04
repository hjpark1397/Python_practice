def kwargs_test(**kwargs): #* 두개 붙이는거 중요!
    print(kwargs)
    print("First value is {first}".format(**kwargs))
    print("Second value is {second}".format(**kwargs))
    print("Third value is {third}".format(**kwargs))

kwargs_test(first=3, second=4, third=5)