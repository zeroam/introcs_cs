"""심화학습 43. 오일러의 거듭제곱의 합 추측
1769년 레온하라트 오일러는 페르의 마지막 정리를 일반화해 n > 2에 대해 정수의 n제곱을 여러개 더해
그 수도 어떤 정수의 n제곱이 되려면 최소한 n개의 n 제곱수가 필요하다고 추측했다.
오일러의 추측을 반증하기 위해 5중으로 내포된 루프를 사용해 어떤 양수 4개의 5제곱의 합이
다른 어떤 수의 5제곱이 되는 수를 찾는 프로그램을 작성하라.
즉, a^5 + b^5 + c^5 + d^5 = e^5를 만족하는 다섯 개의 정수 a, b, c, d, e를 찾아라
"""
import math


def find_five_power_num():
    a = 0
    limit = 50  # 50까지 에서는 안나옴
    while True:
        a += 1
        a_pow = math.pow(a, 5)

        b = 0
        while True:
            b += 1
            b_pow = math.pow(b, 5)

            c = 0
            while True:
                c += 1
                c_pow = math.pow(c, 5)

                d = 0
                while True:
                    d += 1
                    d_pow = math.pow(d, 5)

                    total = a_pow + b_pow + c_pow + d_pow
                    e = 0
                    while True:
                        e += 1
                        e_pow = math.pow(e, 5)
                        if total == e_pow:
                            print(f"solution => a: {a}, b: {b}, c: {c}, d: {d}, e: {e}")
                            return
                        elif e_pow > total:
                            break

                    if d > limit:
                        break
                if c > limit:
                    break
            if b > limit:
                break
        print(f"a: {a}, ... finished")
        if a > limit:
            break


if __name__ == "__main__":
    find_five_power_num()
