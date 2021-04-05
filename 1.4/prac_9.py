"""연습문제 9
다음 각 조건에서 기존 2차원 배열 a[][]의 사본 b[][]를 생성하는 코드 부분을 작성하라.
b 의 답은 a 조건에서도 작동해야 하며, c 의 답은 b 와 c 조건에서도 작동해야 한다.
a. a는 정방행렬이다.
b. a는 일반적인 행렬이다.
c. a가 비균일 배열일 수 있다.
"""
from typing import List


def copy_array(arr: List[List[int]]):
    ret = []
    for row in arr:
        copy_row = []
        for col in row:
            copy_row.append(col)
        ret.append(copy_row)

    return ret


def check_solution(arr: List[List[int]]):
    copy_arr = copy_array(arr)

    assert arr is not copy_arr

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            assert arr[i][j] == copy_arr[i][j]


if __name__ == "__main__":
    # a
    a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    check_solution(a)
    print("test a succeed")

    # b
    b = [[1, 2, 3, 4], [2, 3, 4, 1], [5, 1, 2, 3]]
    check_solution(b)
    print("test b succeed")

    # b
    c = [[1, 2, 5, 3, 4], [3, 4, 1], [5, 1, 2, 3]]
    check_solution(c)
    print("test c succeed")
