"""연습문제 16
명령 줄에서 인수로 두 개의 정수 a와 b를 입력받아
a와 b 사이의 정수 난수를 출력하는 프로그램을 작성하라.
"""
import random
import sys
import stdio

a = int(sys.argv[1])
b = int(sys.argv[2])

num = random.randrange(a, b)
stdio.writeln(num)
