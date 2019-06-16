# 상속(inheritance)
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Korean(Person): #Person 클래스 상속을 받음
    pass            #별도의 구현없이 클래스만 존재하게 해줌

first_korean = Korean("Sungchul", 35)
print(first_korean.name)
