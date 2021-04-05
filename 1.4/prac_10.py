"""연습문제 10
2차원 배열의 전치행렬(행과 열이 바뀐 행렬)을 생성하는 코드 조각을 작성하라.
"""
from typing import List
from pprint import pprint


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    row = len(matrix)
    col = len(matrix[0])
    t_matrix = [[0] * row for _ in range(col)]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            t_matrix[j][i] = matrix[i][j]

    return t_matrix


if __name__ == "__main__":
    matrix = [
        [99, 85, 98],
        [98, 57, 78],
        [92, 77, 76],
        [94, 32, 11],
        [99, 34, 22],
        [90, 46, 54],
        [76, 59, 88],
        [92, 66, 89],
        [97, 71, 24],
        [89, 29, 38]
    ]
    pprint(transpose(matrix))
