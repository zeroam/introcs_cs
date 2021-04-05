"""연습문제 3
실수의 1차원 배열에 들어 잇는 요소들을 역순으로 바꾸는 코드 조각을 작성하라.
결과를 저장하기 위한 별도의 배열은 생성하지 마라.
"""
from typing import List


def reverse_array(array: List[int]) -> List[int]:
    n = len(array)

    for i in range(n // 2):
        temp = array[i]
        array[i] = array[n - i - 1]
        array[n - i - 1] = temp

    return array


if __name__ == "__main__":
    # case 1
    array = [1, 2, 3, 4, 5]
    expect = [5, 4, 3, 2, 1]
    assert reverse_array(array) == expect

    # case 2
    array = [2, 5, 9, 10, 3, 1]
    expect = [1, 3, 10, 9, 5, 2]
    assert reverse_array(array) == expect
