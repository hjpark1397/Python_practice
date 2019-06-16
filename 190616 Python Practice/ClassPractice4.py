class Employee(object):

   raise_amount = 1.1 # 클래스 변수 정의 (인상률)
   num_of_emps = 0 # 클래스 변수 정의 (직원수)
  # 클래스 변수를 사용하면 인스턴스 변수로 관리하기 힘든 데이터를 쉽게 관리할 수 있음
   def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@schoolofweb.net'
        Employee.num_of_emps +=1 # 인스턴스가 생성될 때마다 1씩 증가

   def __del__(self):
       Employee.num_of_emps -=1 # 인스턴스가 제거될 때마다 1씩 감소

   def full_name(self):
        return '{} {}'.format(self.first, self.last)

   def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # 클래스 변수 사용

print(Employee.num_of_emps) # 처음 직원 수
emp_1 = Employee('Sanghee', 'Lee', 50000) # 직원 한명 입사
emp_2 = Employee('Minjung', 'Kim', 60000) # 직원 한명 입사사
print(Employee.num_of_emps) # 직원 수 확인

emp_.raise_amount = 1.2 #인스턴스 변수를 이용하여 특별 인상률 적용

print('# emp_1 연봉 20% 인상')
print(emp_1.pay) # 기존 연봉
emp_1.apply_raise() # 인상률 적용
print(emp_1.pay) # 오른 연봉

print('# emp_2 연봉 10% 인상')
print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)

del emp_1 # 직원 한명 퇴사
del emp_2 # 직원 한명 퇴사
print(Employee.num_of_emps) # 직원 수 확인