"""연습문제 2
[프로그램 1.2.4]의 quadratic.py를 참조해. 다항식 ax^2 + bx + c의 근을 구해 출력하고,
판별식이 음수인 경우에는 적절한 오류 메시지를 출력하고, a가 0일 때는 0으로 나누지 않고 적절히 처리하도록
프로그램을 개선하라
"""
import math
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a == 0:
    x = -c / b
    print(f"x: {x}")
    sys.exit(0)

discrimanant = b * b - 4.0 * a * c
if discrimanant < 0:
    print("there's no solution")
    sys.exit(1)

d = math.sqrt(discrimanant)
x = []
x.append((-b + d) / 2.0 * a)
x.append((-b - d) / 2.0 * a)

print(f"x: {x}")
