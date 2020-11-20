"""1.3.7 - 이진수로 변환"""
import sys
import stdio

n = int(sys.argv[1])

# n보다 작거나 같은 수중 가장 큰 2의 거듭제곱수 v 계산
v = 1
while v * 2 <= n:
    v = v * 2

# v를 반으로 줄이면서 루프를 반복한다.
while v > 0:
    if n < v:
        stdio.write(0)
    else:
        stdio.write(1)
        n -= v
    v = v // 2

stdio.writeln()
