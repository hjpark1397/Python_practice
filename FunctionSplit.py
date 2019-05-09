items = 'zero one two three'.split()
print(items)

example = 'python, jquery, javascript' # ","를 기준으로 문자열 나누기
example.split(",")
print(example)

a, b, c = example.split(",") #리스트 값을 a, b, c로 언패킹
print(a, b, c)

example = 'theteamlab.univ.edu' # "."을 기준으로 문자열 나누기 - 언패킹
subdomain, domain, tld = example.split('.')
print(subdomain, domain, tld)