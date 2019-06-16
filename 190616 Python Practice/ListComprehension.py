# 일반적인 반복문 + 리스트
result = []
for i in range(10):
    result.append(i)

print(result)

# 리스트 컴프리헨션
reult = [i for i in range(10)]
print(result)

# 필터링
# 짝수만 저장하는 코드
result = []
for i in range(10):
    if i % 2 ==0:
        result.append(i)

print(result)

# 필터링 리스트컴프리헨션
result = [i for i in range(10) if i % 2 == 0]
print(result)
#해당 조건을 만족하면 i를 추가할 수 있다.

# else문과 함께 사용하여 해당 조건을 만족하지 않을 때 else 뒤에 i 값을 할당하는 코드
result = [i if i % 2 == 0 else 10 for i in range(10)]
print(result)

# 중첩 반복문
word_1 = "Hello"
word_2 = "World"
result = [i+j for i in word_1 for j in word_2]
print(result)

#중첩 반복문에서 필터링
case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
result = [i+j for i in case_1 for j in case_2 if not (i==j)]
print(result) # 결과 : ['AD', 'AE', 'BD', 'BE', 'BA', 'CD', 'CE', 'CA']

#이차원 리스트 1. 대괄호 두개 사용
words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
# 결과 : ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

#이차원 리스트 2. for문 2개를 붙여서 사용(주의사항 : 대괄호의 위치에 따라 for문의 실행이 달라짐)

#이것은 일차원 리스트 형태
case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
result = [i+j for i in case_1 for j in case_2]
print(result)
# 결과 : ['AD', 'AE', 'AA', 'BD', 'BE', 'BA', 'CD', 'CE', 'CA']

# 이것이 이차원 리스트 형태
# 뒤의 for문이 먼저 고정되낟. 즉, A부터 고정되는 것이 아니라 case_2의 첫번째 요소인 D가 고정,
# A,B,C가 차례로 D 앞에 붙는다
result = [[i+j for i in case_1] for j in case_2]
print(result)
# 결과 : [['AD', 'BD', 'CD'], ['AE', 'BE', 'CE'], ['AA', 'BA', 'CA']]

#리스트 컴프리헨션의 성능
#일반적인 반복문 + 리스트로 구현한 벡터와 스칼라의 곱셈을 실행하는 코드

def sclar_vector_product(scalar, vector):
    result = []
    for value in vector:
        result.append(scalar * value)
    return result

iteration_max = 10000
scalar = 2

for _ in range(iteration_max):
    sclar_vector_product(scalar, vector)

#리스트 컴프리헨션으로 구현한 벡터와 스칼라의 곱셈을 실행하는 코드
iteration_max =  10000
vector = list(range(iteration_max))
scalar = 2

for _ in range(iteration_max):
    [scalar * value for value in range(iteration_max)]