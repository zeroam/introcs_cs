"""연습문제 21
for 루프 안에 while 루프를 사용하는 gamler.py 프로그램을 수정해, 
while 루프 두 개를 사용하거나 for 루프 두 개를 사용하도록 변경하라
"""
import random
import sys
import stdio

stake = int(sys.argv[1])  # 초기 판돈
goal = int(sys.argv[2])  # 목표액
trials = int(sys.argv[3])  # 시뮬레이션 횟수

bets = 0
wins = 0
trial = 0
while trial < trials:
    # 도박 한 판을 진해한다.
    cash = stake
    while (cash > 0) and (cash < goal):
        # 한 번의 베팅을 시뮬레이션한다.
        bets += 1
        if random.randrange(0, 2) == 0:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1

    trial += 1

stdio.writeln(str(100 * wins // trials) + "% 이김")
stdio.writeln("평균 베팅 수: " + str(bets // trials))
