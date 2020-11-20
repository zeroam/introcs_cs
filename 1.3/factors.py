"""1.3.9 - 소인수 분해"""
import sys
import stdio

n = int(sys.argv[1])

factor = 2
while factor * factor <= n:
    while (n % factor) == 0:
        # 소인수로 나눈 후 소인수를 출력한다.
        n //= factor
        stdio.write(str(factor) + " ")
    factor += 1

if n > 1:
    stdio.write(n)
stdio.writeln()
