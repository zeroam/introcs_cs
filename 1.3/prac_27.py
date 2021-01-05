"""연습문제 27
명령 줄 인수로 정수 n을 입력받고, 루프 안에 루프를 넣어 2차원 n x n 크기의 체프판 모양을
출력하는 프로그램 checkerboard.py 프로그램을 작성하라. n이 5일 때 5 x 5 패턴은 다음과 같다.

*  *  *  *  *
 *  *  *  *
*  *  *  *  *
 *  *  *  *
*  *  *  *  *

"""
import sys

n = int(sys.argv[1])

for i in range(n):
    if i % 2 == 0:
        print("*", end="")

    for j in range(n - 1):
        print(" *", end="")
    print()
