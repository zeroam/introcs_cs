"""1.3.6 - 뉴턴 방법"""
import sys
import stdio

EPSILON = 1e-15

c = float(sys.argv[1])
t = c
while abs(t - c/t) > (EPSILON * t):
    # t를 t와 c/t의 평균값으로 설정한다.
    t = (c/t + t) / 2.0

stdio.writeln(t)
