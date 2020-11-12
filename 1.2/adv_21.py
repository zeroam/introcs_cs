"""심화문제 21 - 연속 복리 이자
적립 연수 t, 원금 P, 연간 이율 r을 명령 줄 인수로 받아, 주어진 이율로 연속 복리 이자를 받을 때 적립 연수가 지난 후에
원리금을 계산하는 프로그램을 작성하라. 원리금은 Pe^rt 공식으로 구할 수 있다 (이때 e는 오일러 상수이다).
"""
import sys
import math
import stdio

t = int(sys.argv[1])  # 적립 연수
P = float(sys.argv[2])  # 원금
r = float(sys.argv[3])  # 연간 이율

money = P * math.exp(r * t)
stdio.writeln(money)
