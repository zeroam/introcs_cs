"""연습문제 31
구표면에 위치한 무작위 점(a, b, c)의 좌표를 출력하는 프로그램을 작성하라.
마사글리아 방법(Marsaglia's method)을 이용하면 구표면 위의 점을 쉽게 생성할 수 있다.
마사글리아 방법은 이번 절 뒤에서 설명한 단위 원판 위의 무작위 점 (x, y)를 선택하고 나서,
a = 2 * x * math.sqrt(1 - x * x - y * y)
b = 2 * math.sqrt(1 - x * x - y * y)
c = 1 - 2 * (x * x + y * y)
로 설정한다.
"""
import math
import random


def get_dir() -> int:
    """절반의 확률로 각각 1, -1 리턴"""
    n = random.random()
    if n < 0.5:
        return -1
    return 1


def create_point(r: int) -> tuple:
    while True:
        x = get_dir() * random.random() * r
        y = get_dir() * random.random() * r
        if x * x + y * y <= r * r:
            break

    return (x, y)


def draw_3d_point(r: int) -> tuple:
    x, y = create_point(r)
    print(f"x, y: {(x, y)}")
    # 코드 실행 에러, 1 대신 r * r ? 값이 너무 커짐
    a = 2 * x * math.sqrt(1 - x * x - y * y)
    b = 2 * math.sqrt(1 - x * x - y * y)
    c = 1 - 2 * (x * x + y * y)

    return (a, b, c)


def draw_plot(r: int, repeat: int) -> None:
    a, b, c = [], [], []
    for _ in range(repeat):
        temp_a, temp_b, temp_c = draw_3d_point(r)
        a.append(temp_a)
        b.append(temp_b)
        c.append(temp_c)

    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")


if __name__ == "__main__":
    draw_plot(5, 50)
