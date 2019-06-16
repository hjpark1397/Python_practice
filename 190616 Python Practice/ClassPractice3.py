class Person(object):   # 부모 클래스 Person 선언
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self): # 메서드 선언
        print("저의 이름은", self.name, "이고요, 제 나이는 ", str(self.age), "살 입니다")

class Employee(Person):     # 부모 클래스 Person으로부터 상속
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender) #부모 객체 사용
        self.salary = salary
        self.hire_date = hire_date # 속성값 추가

    def do_work(self): # 새로운 메서드 추가
        print("열심히 일을 한다.")

    def about_me(self): # 부모 클래스 함수 재정의 (오버라이딩)
        super().about_me() # 부모 클래스 함수 사용
        print("제 급여는", sel.salary, "원이고, 제 입사일은", self.hire_date, "입니다.")