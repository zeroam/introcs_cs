"""1.3.5 - 조화급수"""
import sys
import stdio

n = int(sys.argv[1])

total = 0.0
for i in range(1, n + 1):
    # i번째 항목을 합계에 더한다.
    total += 1.0 / i
stdio.writeln(total)
