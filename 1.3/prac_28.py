"""연습문제 28
유클리드 알고리즘을 이용해 두 정수의 최대공약수(GCD)를 구하는 gcd.py 프로그램을 작성하라.
유클리드 알고리즘은 반복적으로 수행하는 방법으로서, x > y일때 y가 x를 나눌 수 있으면 
x와 y의 최대공약수는 y, 나눌 수 없는 경우에는 x와 y의 GCD는 x % y의 GCD와 같다는 성질을 이용한다.
"""
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])

if x < y:
    x, y = y, x

while x % y != 0:
    x = x % y
    x, y = y, x

print(f"최대 공약수: {y}")
