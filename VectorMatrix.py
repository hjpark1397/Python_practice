#선형대수학 연산 가능! 리스트가 있기 때문
#벡터를 파이썬 스타일 코드로 표현하는 방법

vector_a = [1, 2, 10] #리스트 표현
vector_b = (1, 2, 10) #튜플 표현
vector_c = { 'x' : 1, 'y' : 1, 'z' : 10} #딕셔너리로 표현한 경우

# 각 데이터의 이름을 함께 표현해야 한다면 딕셔너리
# 데이터의 위치나 순서가 바뀌지 않아야 한다면 튜플
# -> 목적에 따라 코드 표현은 다를 수 있다

# 연산을 하기 위해서는 먼저 벡터의 크기가 같아야 한다. 벡터를 리스트로 생각한다면, 각 인덱스 값이 같은 위치에 있는 값끼리 연산을 하면 된다


# 벡터의 연산
u = [2, 2]
v = [2, 3]
z = [3, 5]
result = []

for i in range(len(u)):
    result.append(u[i] + v[i] + z[i])

print(result)

# 리스트 컴프리헨션과 zip()을 이용해서
# zip함수는 한개 이상의 리스트 값이 같은 인덱스에 있을 때 병렬로 묶는 함수
u = [2, 2]
v = [2, 3]
z = [3, 5]

result  = [sum(t) for t in zip(u, v, z)] #변수 t에는 차례대로 (2, 2, 3), (2, 3, 5)
print(result)

[t for t in zip(u, v, z)] #변수에 할당 된 것이 무엇인지 확인하기
print([t for t in zip(u, v, z)])

# 별표를 사용한 함수화
def vector_addition(*args):
    return [sum(t) for t in zip(*args)] # [sum(t) for t in zip(u, v, z)]와 같은 효과

vector_addition(u, v, z)

#스칼라-벡터 연산
u = [1, 2, 3]
v = [4, 4, 4]
alpha = 2

result = [alpha * sum(t) for t in zip(u, v)] # alpha는 스칼라값이다 행렬에 곱해주는거!
print(result)

# 행렬의 연산
matrix_a = [[3, 6], [4, 5]]
matrix_b = [[5, 8], [6, 7]]
result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]

print(result)

# 행렬의 동치 = 두개의 행렬이 서로 같은지 나타내는 표현
matrix_a = [[1, 1], [1, 1]]
matrix_b = [[1, 1], [1, 1]]
all([row[0]==value for t in zip(matrix_a, matrix_b) for row in zip(*t) for value in row])
print(all([row[0]==value for t in zip(matrix_a, matrix_b) for row in zip(*t) for value in row]))
#같으니까 true 출력

matrix_b = [[5, 8], [6, 7]]
all([row[0]==value for t in zip(matrix_a, matrix_b) for row in zip(*t) for value in row])
print(all([row[0]==value for t in zip(matrix_a, matrix_b) for row in zip(*t) for value in row]))
#다르므로 false 출력

#all( )함수와 any( )함수는 리스트형과 튜플형에서 내부 값이 and 조건이나 or 조건으로 참인지 거짓인지 반환하는 함수

#전치행렬
matrix_a = [[1, 2, 3], [4, 5, 6]]
result = [[element for element in t] for t in zip(*matrix_a)]
#각 행과 같은 위치의 인덱스 값 추출하고 리스트를 새롭게 구성
print(result)

#행렬의 곱셈
matrix_a = [[1, 1, 2], [2, 1, 1]]
matrix_b = [[1, 1], [2, 1], [1, 3]]
result = [[sum(a*b for a, b in zip(row_a, column_b)) for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)

#제일 복잡한듯