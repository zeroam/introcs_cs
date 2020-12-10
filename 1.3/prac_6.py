"""연습문제 6
tenshellos.py의 구조를 바꾸어 출력할 줄 수를 명령 줄 인수로 입력받는 hellos.py 프로그램을
작성하라. 인수는 1000보다 작다고 가정한다.
"""
import sys

count = int(sys.argv[1])

# https://www.thoughtco.com/what-is-an-ordinal-number-1691459
for i in range(1, count + 1):
    if i % 10 == 1:
        prefix = "st"
    elif i % 10 == 2:
        prefix = "nd"
    elif i % 10 == 3:
        prefix = "rd"
    else:
        prefix = "th"

    # exception
    if i % 100 in [11, 12, 13]:
        prefix = "th"

    print(f"{i}{prefix} Hello")
