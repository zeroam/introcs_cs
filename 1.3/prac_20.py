"""연습문제 20
양의 정수 n의 이진 표현을 문자열 s로 변환하는 코드 조각을 작성하라
"""
import sys

n = int(sys.argv[1])

s = ''
while n > 0:
    s = str(n % 2) + s
    n //= 2
print(s)
