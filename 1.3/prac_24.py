"""연습문제 24
gambler.py를 수정해 도박꾼의 최대 베팅 수를 명령 주 인수에서 입력받도록 변경하라.
그러면 게임은 도박꾼의 승리, 파산, 혹은 횟수 초과 , 세 가지 중 하나로 끝나게 된다.
횟수가 초과될 때는 도박꾼에게 남은 돈도 출력하라.
보너스 점수: 이 프로그램을 이요앻 카지노에 도박하러 갈 계획을 수립하라.
"""
import random
import sys
import stdio

stake = int(sys.argv[1])  # 초기 판돈
goal = int(sys.argv[2])  # 목표액
trials = int(sys.argv[3])  # 시뮬레이션 횟수
max_bet = int(sys.argv[4])  # 최대 베팅 수

total_bets = 0
wins = 0
max_out = 0
remain = 0
for i in range(trials):
    # 도박 한 판을 진행한다.
    cash = stake
    bets = 0
    while (cash > 0) and (cash < goal):
        # 한 번의 베팅을 시뮬레이션한다.
        if bets > max_bet:
            max_out += 1
            remain += cash
            break

        if random.randrange(0, 2) == 0:
            cash += 1
        else:
            cash -= 1
        bets += 1
        total_bets += 1

    if cash == goal:
        wins += 1

win_rate = (100 * wins) / trials
max_out_rate = (100 * max_out) / trials
print(f"승률: {win_rate:.2f}%, 파산: {100 - win_rate - max_out_rate:.2f}%, 횟수 초과: {max_out_rate:.2f}%")
print(f"평균 베팅 수: {total_bets / trials:.2f}, 평균 남은 금액: {remain / max_out:.2f}")

