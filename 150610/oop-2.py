class Employee(object):
    pass

emp_1 = Employee()
emp_2 = Employee()

#인스턴스 변수에 데이터 저장
emp_1.first = 'Sanghee'
emp_1.last = 'Lee'
emp_1.email = 'sanghee.lee@schoolofweb.net'
emp_1.pay = 50000

emp_2.first = 'Minjung'
emp_2.last = 'Kim'
emp_2.email = 'minjung.kim@schoolofweb.net'
emp_2.pay = 60000

#인스턴스 변수 데이터에 엑세스
print(emp_1.email)
print(emp_2.email)