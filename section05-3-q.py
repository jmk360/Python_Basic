# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
print(q1.get('가을'))

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
if "사과" in q2.values():
    print('사과 있음')
# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
score = 89
grade = ''
if 80 < score <= 100:
    grade = 'A'
elif 60 < score <= 80:
    grade = 'B'
elif 40 < score <= 60:
    grade = 'C'
elif 20 < score <= 40:
    grade = 'D'
else:
    grade = 'E'
print('학점 :', grade)
# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a, b, c = 12, 6, 18
if a > b:
    if a > c:
        print('가장 큰 수 :', a)
    else:
        print('가장 큰 수 :', c)
else:
    if b > c:
        print('가장 큰 수 :', b)
    else:
        print('가장 큰 수 :', c)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
s = '891022-2473837'
if s[7] == 1 or s[7] == 3:
    print('남자')
else:
    print('여자')

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
for q in q3:
    if q == '정':
        continue
    print(q)
# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for n in range(1,101,2):
    print(n,end=' ')
print()

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
for q in q4:
    if len(q) >= 5:
        print(q)
# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for q in q5:
    if q.islower():
        print(q)

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
data_list = []
for q in q6:
    if q.islower():
        data_list.append(q.upper())
    else:
        data_list.append(q.lower())
print(data_list)


# list conprehension

numbers = []
for n in range(1,101):
    numbers.append(n)

print(numbers)

numbers2 = [n for n in range(1, 101)]
print(numbers2)

q3 = ["갑", "을", "병", "정"]
list_data = [x for x in q3 if x != '정']
print(list_data)

# list_data = [x for x in range(1,101,2)]
list_data = [x for x in range(1,101) if x % 2 != 0]
print(list_data)