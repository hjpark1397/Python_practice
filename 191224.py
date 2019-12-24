# #스포애니 헬스장 문제
#
# menu = ['가입비', '3개월 등록', '6개월 등록', '1년 등록', '운동복 대여', '사물함 대여']
# price = [30000, 90000, 150000, 240000, 10000, 5000]
# #위 리스트를 이용하여 아래와 같이 가격표를 출력하기
# print('-----------가격표-------------')
# for i in range(len(menu)):
#     print(f'{menu[i]} : {price[i]}원')
# print('------------------------------')
#
# import random
# number = 0
# while True:
#     number = random.randint(1,3)
#     print(f'랜덤한 숫자를 뽑습니다. : {number}')
#
#     if number==2:
#         break
#
# def Star(character, height):
#     for i in range(int(height)):
#         print(character*i)
# char = input('문자를 입력하세요. : ')
# height = input('높이를 입력하세요. : ')
# Star(char, height)
#
# def inch_to_cm(inch):
#     return inch * 2.54
#
# inch = int(input('인치를 입력하세요. : '))
# cm = inch_to_cm(inch)
# print(f'{inch}in => {cm}cm')

#오늘은 크리스마스 이브니까 별찍기
print(' ')
print('=========== Merry Christmas =========')
for i in range(0, 4):
    print(' ' * (7 - i + 12) + '*' * (2 * i - 1))
for i in range(1, 5):
    print(' ' * (6 - i + 12) + '*' * (2 * i + 1))
for i in range(3, 7):
    print(' ' * (6 - i + 12) + '*' * (2 * i + 1))
for i in range(4):
    print(' ' * 17 + '*' * 3)

#여러 숫자 입력하기 리스트로 여러개 입력하기.전부다 숫자로
numbers = []
for n in input('숫자를 많이 입력해보세요').split():
    numbers.append(int(n))

print(numbers)

#사용자에게 여러 입력 받아서 덧셈 결과 얻어보기
def add_multi(numbers):
    total = 0
    for n in numbers:
        total += int(n)

    return total

user_input = input('숫자를 여러개 입력해보세요. : ').split()
total = add_multi(user_input)

print(total)