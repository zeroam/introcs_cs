"""연습문제 23
gambler.py를 수정해 매번 베팅할 때마다 도박꾼이 이길 고정 확률을 명령 줄 인수에서 입력받도록 변경하라.
이 프로그램을 이용해 이 확률이 우승 확률과 예상 베팅 수에 어떤 영향을 미치는 지 살펴보라.
확률 p를 0.48 등 0.5에 가깝게 설정해 시험해보라
"""
import random
import sys
import stdio

stake = int(sys.argv[1])  # 초기 판돈
goal = int(sys.argv[2])  # 목표액
trials = int(sys.argv[3])  # 시뮬레이션 횟수
p = float(sys.argv[4])  # 도박꾼이 이길 고정 확률

bets = 0
wins = 0
for i in range(trials):
    # 도박 한 판을 진행한다.
    cash = stake
    while (cash > 0) and (cash < goal):
        # 한 번의 베팅을 시뮬레이션한다.
        bets += 1
        if random.random() <= p:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1

stdio.writeln(str(100 * wins // trials) + "% 이김")
stdio.writeln("평균 베팅 수: " + str(bets // trials))
