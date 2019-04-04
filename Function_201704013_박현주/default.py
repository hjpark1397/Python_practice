def print_something_2(my_name, your_name="TEAMLAB"):#매개변수 기본값이 TEAMLAB
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_something_2("hyunjoo", "TEAMLAB")
print_something_2("hyunjoo")#2개를 받으나 하나만 입력됨. 팀 랩은 디폴트값으로 출력