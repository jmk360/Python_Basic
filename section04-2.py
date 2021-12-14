'''
문자형 관련 연산자

문자열 생성, 길이
이스케이프 문자
문자열 연산
문자열 형 변환
문자열 함수
문자열 슬라이싱
'''

# Section04-2
# 문자열 ,문자열연산, 슬라이싱

str1 = "I am Boy."
str2 = 'NiceMan'
str3 = ' '
str4 = str()
print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)

escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String -> 경로 같은 경우에서 많이 사용
raw_s1 = r"C:\Programs\Test\Bin"
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인
multi = \
"""
문자열
멀티라인
테스트
"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3)
print("a" in str_o4)
print("f" in str_o4)
print("z" not in str_o4)

# 문자열 형 변환
print(str(77) + 'a')
print(str(10.4))

# 문자열 함수

a = 'niceman'
b = 'orange'

print(a.islower())
print(a.isupper())
print(b.endswith('e'))
print(a.capitalize())
print(a.replace('nice', 'good'))
print(list(reversed(b)))

a = 'niceman'
b = 'orange'

print(a[0:3]) # 0 <= index < 3
print(a[0:4])
print(a[0:7])
print(a[0:len(a)-1])
print(a[:])
print(b[0:4:2])
print(b[1:-2])
print(b[::-1])