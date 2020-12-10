"""연습문제 10
숫자 n = 2, 4, 8, 16, 32, 64, ..., 2048에 대해 log2n, n, nlogen, n^2, n^3, 2^n
을 표 형태로 출력하는 프로그램 functiongrowth.py를 작성하라. 탭(\t) 문자를 이용하면 세로로 줄을 맞출 수 있다.
"""
import math

nums = [2 ** n for n in range(1, 11)]
for n in nums:
    print(f"|log2n:{math.log2(n):>5}", end="")
    print(f"|n:{n:>5}", end="")
    print(f"|nlogen:{n * math.log(n):>8.2f}", end="")
    print(f"|n^2: {n ** 2:>8}", end="")
    print(f"|n^3: {n ** 3:>12}", end="")
    print(f"|2^n: {2 ** n:>80}|")
