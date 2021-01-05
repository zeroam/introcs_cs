"""연습문제 22
도박꾼이 베팅할 때마다 가진 돈으 $1당 별표 하나로 출력해 도박꾼의 파산  시뮬레이션을
추적하는 gamblerplot.py 프로그램을 작성하라
"""
import random
import sys
import stdio

stake = int(sys.argv[1])  # 초기 판돈
goal = int(sys.argv[2])  # 목표액
trials = int(sys.argv[3])  # 시뮬레이션 횟수

bets = 0
wins = 0
for i in range(trials):
    # 도박 한 판을 진해한다.
    print(f"trial: {i} started!")

    cash = stake
    while (cash > 0) and (cash < goal):
        # 한 번의 베팅을 시뮬레이션한다.
        bets += 1
        if random.randrange(0, 2) == 0:
            cash += 1
        else:
            cash -= 1
        print("*" * cash)
    if cash == goal:
        wins += 1
        
    print()

stdio.writeln(str(100 * wins // trials) + "% 이김")
stdio.writeln("평균 베팅 수: " + str(bets // trials))
