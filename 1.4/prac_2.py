"""연습문제 2
길이가 n이고 1차원 배열로 표현된 두 개의 벡터가 있을 때,
이 둘 간의 유클리드 거리를 구하는 코드부분을 작성하라
"""
import math
from typing import Tuple


def get_dist(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    return math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))


if __name__ == "__main__":
    print(get_dist((3, 6), (7, 3)))
