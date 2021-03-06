"""1.3.9 - 소인수 분해"""
import sys
import stdio
import time

n = int(sys.argv[1])

start = time.time()
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

print(f"elapsed: {time.time() - start:.4f}s")
