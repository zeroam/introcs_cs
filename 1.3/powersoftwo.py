"""1.3.3 2의 거듭제곱 계산하기"""
import sys
import stdio

n = int(sys.argv[1])
power = 1
i = 0
while i <= n:
    # 2의 n제곱을 출력한다.
    stdio.writeln(str(i) + " " + str(power))
    power = 2 * power
    i = i + 1
