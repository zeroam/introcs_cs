"""심화문제 34 - 소수세기
명령 줄 인수로 정수 n을 입력받아 n보다 작거나 같은 소수의 개수를 출력하는 프로그램 primecounter.py를 작성하라.
이 프로그램을 이용해 천만보다 작거나 같은 소수를 출력해보라.
"""
import sys


# 에라토스테네스의 체
def prime_list(n: int) -> list:
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] is True:
            for j in range(i + i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] is True]


n = int(sys.argv[1])

print(len(prime_list(n)))
