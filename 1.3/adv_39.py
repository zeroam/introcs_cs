"""심화학습 39 - 실험 분석
[심화학습 37]에서 구현한 3가지 e^x 계산 방법
1. 내포된 for 루프를 이용한 직접 계산 방법
2. 단일 while 루프로 개선한 방법
3. term > 0 종료 조건을 이용한 방법
"""
import time
import math
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_at = time.time()
        cnt = 0
        while time.time() - start_at < 10:
            ret = func(*args, **kwargs)
            cnt += 1

        print(f"{func.__name__}: {ret}, {cnt} repeated")

        return ret

    return wrapper


@timeit
def solution_1(x: float):
    term = 1.0
    total = 0.0
    n = 1
    while total != total + term:
        total += term
        term = 1.0
        for i in range(1, n + 1):
            term *= x / i
        n += 1

    return total


@timeit
def solution_2(x: float):
    term = 1.0
    total = 0.0
    n = 1
    while total != total + term:
        total += term
        term *= x / n
        n += 1

    return total


@timeit
def solution_3(x: float):
    term = 1.0
    total = 0.0
    n = 1
    while term > 0:
        total += term
        term *= x / n
        n += 1

    return total


@timeit
def solution_mathlib(x: float):
    return math.exp(x)


if __name__ == "__main__":
    import sys

    x = float(sys.argv[1])

    solution_1(x)
    solution_2(x)
    solution_3(x)
    solution_mathlib(x)
