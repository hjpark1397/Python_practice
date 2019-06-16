# 파이썬의 객체 지향 프로그래밍
# 클래스 구현하기 ( 인공지능 축구 프로그램 만들기 )

# class SoccerPlayer(object): #class(클래스 예약어) SoccerPlayer(클래스 이름) (object) : 상속받는 객체명
#     def __init__(self, name, position, back_number): #__init__() 속성에 대한 정보를 선언하는 예약 함수
#         self.name = name                            # 첫번째 매개변수는 반드시 self 사용
#         self.position = position                    # self 변수 : 클래스에서 생성된 인스턴스에 접근하는 예약어
#         self.back_number = back_number
#     #함수 선언
#     def change_back_number(self,new_number):
#         print("선수의 등번호를 변경한다 : From %d to %d" % (self.back_number, new_number))
#         self.back_number = new_number
#
#     def __str__(self):
#         return "Hello, My name is %s. I play in %s in center." %(self.name, self.position)
#
# #SocfcerPlayer를 사용하는 instance 코드
# jinhyun = SoccerPlayer("Jinhyun", "MF", 10) #객체명, 클래스 이름, (__init__함수 interface, 초깃값)
#
# print("현재 선수의 등번호는 : ", jinhyun.back_number)
# jinhyun.change_back_number(5) # 등 번호를 바꿔줌
# print("현재 선수의 등번호는 : ", jinhyun.back_number)
#
# print(jinhyun) # __str__함수로 선언된 부분이 print() 함수를 사용하면 반환되는 함수
#                # __str__함수 : 인스턴스의 정보를 표시하거나 구분할 때 사용 -> 예약함수는 특정 조건에서 작동

#객체지향 프로그래밍 연습
#데이터
names = ["Messi", "Ramos", "Ronaldo", "Park", "Buffon"]
positions = ["MF", "DF", "CF", "WF", "GK"]
numbers = [10, 4, 7, 13, 1]

#이차원 리스트
players = [[name, position, number] for name, position, number in zip(names, positions, numbers)]
print(players)
print(players[0])

#전체 SoccerPlayer 코드
class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경한다 : From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number

    def __str__(self):
        return "Hello, Myname is %s. I play in %s in center." % (self.name, self.position)

#클래스 인스턴스
player_objects = [SoccerPlayer(name, position, number) for name, position, number in zip(names, positions, numbers)]
print(player_objects[0])