result = []
for i in range(10):
    result.append(i)

print(result)
# 위는 반복문으로 리스트를 찍어내는 것
result = [i for i in range(10)]

print(result)
# 리스트 컴프리헨션 - 리스트와 for문을 한 줄에 사용할 수 있다는 장점!

#range()함수를 사용하여 0부터 9까지 숫자를 생성하고, result 변수에 추가하는 코드.

#짝수 저장하기(for 문)
result = []
for i in range(10):
    if i%2==0:
        result.append(i)

print(result)

#짝수 저장하기(리스트 컴프리헨션)
result = [i for i in range(10) if i%2==0]
print(result)

#필터링
result = [i if i%2==0 else 10 for i in range(10)]
print(result)
#기존 list comprehension문제 if i % 2==0을 삽입하여 해당조건을 만족할 때만 i추가
# else문을 사용하여 만족하지 않을 경우에는 다른 값을 할당

#중접 반복문
word_1="Hello"
word_2="World"
result = [i+j for i in word_1 for j in word_2]
print(result)
#word_1에서 나오는 값 고정 후 word_2 값을 하나씩 가져와 결과 생성

#중첩 반복문 필터링
case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
result = [i+j for i in case_1 for j in case_2 if not(i==j)]
print(result)

#이차원 리스트
words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)

stuff = [[w.upper(), w.lower(), len(w)] for w in words] #리스트의 각 요소를 대문자, 소문자, 길이로 변환하여 이차원 리스트로 변환
for i in stuff:
    print(i)

case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
result = [i+j for i in case_1 for j in case_2]
print(result)

result = [[i+j for i in case_1] for j in case_2]
print(result)


