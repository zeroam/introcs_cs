"""프로그램 1.4.3 - 에라토스테네스의 체"""
import math
import sys
import time

import stdarray
import stdio


def timeit(func):
    def wrapper(*args, **kwargs):
        start_at = time.time()
        ret = func(*args, **kwargs)
        print(f"{func.__name__} finished in {time.time() - start_at}s")
        return ret

    return wrapper


@timeit
def sieve_origin(n):
    isPrime = stdarray.create1D(n + 1, True)

    for i in range(2, n):
        if (isPrime[i]):
            # i의 배수 인덱스 요소들은 모두 소수가 아니라고 표시한다.
            for j in range(2, n // i + 1):
                isPrime[i * j] = False

    # 소수의 개수를 센다
    count = 0
    for i in range(2, n + 1):
        if (isPrime[i]):
            count += 1

    return count


@timeit
def sieve_sqrt_cond(n):
    isPrime = stdarray.create1D(n + 1, True)

    # 종료조건 변경
    for i in range(2, int(math.sqrt(n)) + 1):
        if (isPrime[i]):
            # i의 배수 인덱스 요소들은 모두 소수가 아니라고 표시한다.
            for j in range(2, n // i + 1):
                isPrime[i * j] = False

    # 소수의 개수를 센다
    count = 0
    for i in range(2, n + 1):
        if (isPrime[i]):
            count += 1

    return count


if __name__ == "__main__":
    n = int(sys.argv[1])

    origin = sieve_origin(n)
    stdio.writeln(f"origin: {origin}")
    sqrt_cond = sieve_sqrt_cond(n)
    stdio.writeln(f"sqrt condition: {sqrt_cond}")
