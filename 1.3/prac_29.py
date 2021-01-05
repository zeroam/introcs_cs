"""연습문제 29
명령 줄 인수로 정수 n 하나를 입력받고 n x n 표를 출력하는 프로그램 relativeprime.py를 작성하라.
i와 j의 GCD가 1(즉 i와 j가 서로소)인 경우 이 표의 항목(i, j)에 별표를, 그렇지 않으면 공백을 넣으면 된다.
"""
import sys

n = int(sys.argv[1])


def get_gcd(x, y):
    if x < y:
        x, y = y, x

    while x % y != 0:
        x = x % y
        x, y = y, x

    return y


for i in range(1, n + 1):
    print(f"{i:3}: ", end="")
    for j in range(1, n + 1):
        word = ""
        if get_gcd(i, j) == 1:
            word = "*"
        else:
            word = " "
        print(word, end=" | ")
    print()
