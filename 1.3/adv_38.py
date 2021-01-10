"""심화학습 38 - 삼각함수
테일러 급수 전개를 이용해 사인을 구하는 sine.py, 코사인을 구하는 cosine.py를 구현하라.
sin x에서 테일러 급수는 x - x^3/3! + x^5/5! - ...
cos x에서 테일러 급수는 1 - x^2/2! + x^4/4! - ... 로 전개한다.
"""


def cal_sin(x: float) -> float:
    term = x
    oper = 1
    n = 3
    total = 0.0
    while total != total + term:
        total += term * oper
        for i in range(n - 1, n + 1):
            term *= x / i

        oper *= -1
        n += 2

    return total


def cal_cos(x: float) -> float:
    term = 1
    oper = 1
    n = 2
    total = 0.0
    while total != total + term:
        total += term * oper
        for i in range(n - 1, n + 1):
            term *= x / i

        oper *= -1
        n += 2

    return total


if __name__ == "__main__":
    import sys

    x = float(sys.argv[1])
    sin_x = cal_sin(x)
    cos_x = cal_cos(x)

    print(f"sin x: {sin_x}")
    print(f"cos x: {cos_x}")
