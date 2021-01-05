"""연습문제 25
factors.py를 수정해 각 소인수를 한 번씩만 출력하도록 변경하라.
"""
import sys

n = int(sys.argv[1])

nums = set()
factor = 2
divide = False
while factor * factor <= n:
    divide = False
    while (n % factor) == 0:
        n //= factor
        divide = True
    if divide:
        print(factor, end=" ")
    factor += 1

if n > 1:
    print(n, end=" ")
print()
