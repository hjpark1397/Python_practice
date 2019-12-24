# i = 0
# while True:
#     print(i)
#     i += 1
#     if i < 10:
#         break

# i = 0
# while True:
#     i += 1
#     print(i)
#
#     if i > 5:
#         break
# #6까지 출력이 되는데, i가 5일때 연산이 되면 6까지 나오니까!
#
# a = 1
# b = 2
# print(f'{a}+{b}={a+b}')
#
# message = 'hello'
# for i in range(10): #0부터 9까지 반복!
#     print(f'{message}{i}')
#
#
# message = input('문자를 하나 입력하세요 : ')
# print(f'당신이 입력한 문자는 \'{message}\'입니다.')

# for value in 'hello world':
#     print(value)
#한 글자씩 한 줄에 출력된다.

print('hello world'[0:2:1])#앞에서부터 두글자만 출력된다.
print('hello world'[:2])#얘도 같은 맥락으로 가능한 것이고먼

'hello world'[0:5:1]
print('hello world'[0:5:1])

print('hello world'[:5])


#문자열 각 자릿 수 합 구하기
total = 0
for v in '123456789':
    total += int(v)
print(total)

#철문제 4번
# def multiple(x, y):#매개변수 x, y
#     x, y = map(int, input('숫자 두 개를 입력하세요 : ').split()) #공백을 기준으로 두 문자를 나누어준다.
#     for v in x:
#         for m in y:
#             total = int(m)*

#리스트를 써보자
fruits = ['apple', 'banana', 'cranberry', 'durian']

for fruit in fruits: # fruits 리스트 안의 요소를 변경할 필요가 없을 때 사용
    print(fruit) #과일이 한종류씩 출력된다.

fruits = ['apple', 'banana', 'cranberry', 'durian']

for i in range(len(fruits)): #fruit의 인덱스를 사용해야할 때 사용한다.
    print(fruits[i])

#enumerate 내장함수 - 카운트와 값 반환

fruits = ['apple', 'banana', 'cranberry', 'durian']

for i, fruit in enumerate(fruits):
    print(f'{i}번째 요소 : {fruit}')#i에는 순서가 담긴다.

#짝수는 -1로 바꾸기
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for index, value in enumerate(a):
#     if value % 2 == 0:
#         a[index] = -1 #짝수일때 -1을 넣어준다.
#
# print(a)
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for index in range(len(a)):
#     if a[index] % 2 == 0:
#         a[index] = -1
#
# print(a)
#
# for i in range(1, 6):
#     print(i) #1시작, 6되면 종료

a = [1,2,3,4,5]
for v in a: #이건 리스트라서 range를 쓰면 안된다.
    print(v)

fruits = ['apple', 'banana', 'green grape']

for i, v in enumerate(fruits):
    print(i, v)

#리스트 항목 추가하기 -> append혹은 insert 이용
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, '**')
print(fruits)

#clear와 del과 같은 기능을 한다.
fruits.clear()
print(fruits)

fruits = ['apple', 'banana', 'cherry']
del fruits[:]
print(fruits)

#index : 요소를 검색해서 인덱스를 반환한다.
fruits = ['apple', 'banana', 'cherry', 'kiwi']
fruits.index('banana')
print(fruits.index('cherry'))#cherry의 인덱스 값을 반환한다. 존재하지 않는 요소를 검색하면 error

for i in range(len(fruits)):#리스트의 길이만큼 순차 탐색을 진행하는 것.
    if fruits[i] == 'cherry':
        print(i)#체리를 찾으면 그 인덱스 값을 반환해준다.

#요소의 개수를 반환하는 count
fruits = ['apple', 'banana', 'cherry', 'cherry', 'cherry']
fruits.count('cherry')
print(fruits.count('cherry'))

#리스트를 정렬하는 sort - 오름차순 정렬
a = [10, 9, 2, 8, 3, 1, 6]
a.sort()
print(a)

#내림차순 sort(revers=True)
a = [1, 2, 6, 7, 3, 8]
a.sort(reverse=True)
print(a)

#리스트 역순으로 = reverse
a = [1, 4, 5, 2]
a.reverse()
print(a)

#copy -> 리스트 복사
a = [1, 2, 3, 4, 5]
b = a.copy() #a를 b에 복사한다.
a.append(6) #a에만 6추가
print(a)
print(b)

#리스트 정리 문제
a = [1, 3, 5, 7, 9]
a.insert(1, 2)
a.insert(3, 4)
a.insert(5, 6)
a.insert(7, 8)
a.insert(9, 10) #각 자리에 값 삽입 완료
a.sort(reverse=True) #내림차순 출력하기
print(a)

#반복문으로 추가하기
a = [1, 3, 5, 7, 9]
for v in range(2, 11, 2):
    a.insert(v-1, v)

print(a)
a.sort(reverse=True)
print(a)

#함수
def add(a, b):
    return a + b

# a, b = map(int, input('두 숫자를 입력하세요. : ').split())
# print(add(a,b))

