'''
파이썬 자료구조(Dictionary, Set)

딕셔너리 특징
딕셔너리 추가
집합 특징
집합 자료형 함수
자료형 변환
'''

# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# key, value
# 선언
a = {'name':'kim', 
    'phone':'010-7777-7777',
    'birth':870214}
b = {
    0:'Hello Pyhton',
    1:"Hello Coding"
}
c = {
    'arr':[1,2,3,4,5]
}

print(type(a))

# 출력
print(a['name'])
print(a.get('name'))
print(a.get('address'))
print(a.get('address', 'default'))
print(c['arr'][1:2])
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1,2,3)
print(a)

# keys, values, items
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(list(a.items()))
print(2 in b)
print('name2' not in a)

# 집합(Sets) (순서x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)

t = tuple(b)
print(t)
l = list(b)
print(l)

print()
print()

s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}

print(s1.intersection(s2))
print(s1 & s2)

print(s1.union(s2))
print(s1 | s2)

print(s1.difference(s2))
print(s1 - s2)

print(s1.symmetric_difference(s2)) # 대칭 차집합

# 추가 & 제거
s3 = {7, 8, 10, 15}
s3.add(18)
s3.add(7)
print(s3)

s3.remove(15)
print(s3)

print(type(s3))