"""연습문제 5
불형 2차원 배열의 내용을 출력하는 코드 조각을 작성하라.
요소의 값이 True이면 '*', 아니면 공백을 출력하되, 행과 열 번호도 출력하라
"""
import random
from typing import List


def make_2dim_array(rows: int, cols: int) -> List[List[bool]]:
    arr = [[False] * cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            # 랜덤으로 True 지정
            if random.random() >= 0.5:
                arr[row][col] = True

    return arr


def print_2dim_array(arr: List[List[bool]]) -> None:
    # print col number
    print("  ", end="|")
    for col_num in range(len(arr[0])):
        print(f"{col_num:02}", end="|")
    print()

    for i, row in enumerate(arr):
        print(f"{i:02}", end="|")
        for col in row:
            word = "  "
            if col is True:
                word = " *"
            print(word, end="|")
        print()


if __name__ == "__main__":
    arr = make_2dim_array(15, 15)
    print_2dim_array(arr)
