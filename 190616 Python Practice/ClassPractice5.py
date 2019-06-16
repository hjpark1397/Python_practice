class Human(object):

    def __init__(self, name, weight): # __init__ 인스턴스를 만들 때 실행되는 함수
        self.name = name
        self.weight = weight

    def __str__(self): # __str__ : 인스턴스 자체를 출력 할 때의 형식을 지정해주는 함수
        return "{} (몸무게 {}kg)".format(self.name, self.weight) #여기서는 문자열화한다!

person = Human("사람", 60.5) # 초기화 함수 사용
print(person) # 문자열화 함수 사용