#전체 SoccerPlayer 코드
class SoccerPlayer(object):
    def __init__(self, name, position,back_number):
        self.name = name
        self.position = position
        self.back_numeber = back_number
    def change_back_number(self, new_number):
        print("선수의 등번호를 변경한다 : From %d to %d")