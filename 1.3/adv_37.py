"""심화학습 37 - 지수 함수
x가 실수라고 가정한다. 테일러 급수 전개를 이용해 e^x = 1 + x + x^2/2 + x^3/3! + ...를 total에 할당하는 코드 조각을 작성하라.
x = x/1
x^2/2 = x/1 * x/2
x^3/3! = x/1 * x/2 * x/3
x^n/n! = x/1 * x/2 * ... * x/n
"""
import sys

x = float(sys.argv[1])

term = 1.0
total = 0.0
n = 1
while total != total + term:
    total += term
    term *= x / n
    n += 1

print(f"e^{x}: {total}")
