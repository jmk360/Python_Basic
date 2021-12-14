# Sectioin02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this
import sys

print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('My name is Goodboy!')

# 변수 선언
myName = 'Badboy'

# 조건문
if myName == 'Goodboy':
    print('ok')
else:
    print('not')

# 반복문
for i in range(1,10,3):
    for j in range(1,10):
        print(f'{i}*{j}={i*j}\t\t{i+1}*{j}={(i+1)*j}\t\t{i+2}*{j}={(i+2)*j}')
    print('='*50)

# 변수 선언(한글)

이름 = "좋은사람"

# 출력
print(이름)

# 함수 선언(한글)

def 인사():
    print("안녕하세요. 반갑습니다.")

인사()

# 함수 선언(영어)
def greeting():
    print('Hello!')

greeting()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))