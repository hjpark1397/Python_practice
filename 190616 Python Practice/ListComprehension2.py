#split() 함수 : 문자열의 값을 특정 값을 기준으로 분리하여 리스트 형태로 반환
items = 'zero one two three'.split() # 빈칸을 기준으로 문자열 분리하기
print(items)

example = 'python,jquery,javascript' # ","을 기준으로 문자열 나누기
example.split(",")

a, b, c = example.split(",") # 리스트에 있는 각 값을 a, b, c 변수로 언패킹
print(a, b, c)

example = 'theteamlab.univ.edu' # "."을 기준으로 문자열 나누기 -> 언패킹
subdomain, domain, tld = example.split('.')
print(subdomain, domain, tld)

#join() 함수 : 문자열로 구성된 리스트를 합쳐 하나의 문자열로 반환
colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors) # 전부 다 붙여서 이어준다
print(result)

result = ' '.join(colors) # 띄어쓰기로 이어준다
print(result)

result = ', '.join(colors) # 콤마 및 띄어쓰기로 이어준다
print(result)

result = '-'.join(colors) # 연결 시 "-"으로 연결
print(result)

# enumerate() 함수 : 리스트 값을 추출할 때 인덱스를 붙여 함께 출력하는 방법
# 주로 딕셔너리형 - 인덱스 : key, 단어를 : value => 쌍으로 묶어 결과를 출력
for i, v in enumerate(['tic', 'tac', 'toe']): # 리스트에 있는 인덱스와 값을 언패킹
    print(i, v)

{i :j for i,j in enumerate('TEAMLAB is an academic institute located in South Korea.'.split())}
print({i :j for i,j in enumerate('TEAMLAB is an academic institute located in South Korea.'.split())})

#zip() 함수 : 한개 이상의 리스트 값이 같은 인덱스에 있을 때 병렬로 묶는 함수
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):              # 병렬로 값을 추출
    print(a,b)

a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)

[sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100,200,300))]
print([sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100,200,300))]) # 같은 위치에 있는 값 더하기

#enumerate() 함수와 zip() 함수 같이 사용
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for i, (a, b) in enumerate(zip(alist, blist)):
    print(i, a, b)
# 같은 인덱스의 값끼리 묶어 출력