"""연습문제 11
명령 줄 인수로 양수 두개를 입력받아 둘 중 하나로 다른 수를 완전히
나눌 수 있으면 True를 출력하는 프로그램을 작성하라
"""
import sys
import stdio

a = int(sys.argv[1])
b = int(sys.argv[2])

if a > b:
    remain = a % b
else:
    remain = b % a

if remain == 0:
    stdio.writeln(True)
else:
    stdio.writeln(False)
