"""심화학습 41 - 게임 시뮬레이션
1970년대 게임쇼 Let's Make a Deal 에서는 도전자에게 세개의 문이 주어졌다.
문 하나의 뒤에는 큰 상이 있다.
도전자가 선택한 후 진행자는 나머지 두 문 중 하나를 열어 보여준다.(물론 상이 있는 문은 열지 않는다.)
그러고 나서 도전자는 열지 않은 다른 문으로 바꿀 수 있는 기회를 가진다.
도전자는 선택을 바꿔야 할까?
얼핏 보면 도전자가 처음 선택한 문이나 열지 않은 문이나 상이 있을 확률은 똑같으므로 선택을 바꿀 필요가 없을 것처럼 보인다.
시뮬레이션을 이용해 이 생각이 맞는지 검사하는 montehall.py 프로그램을 작성하라
프로그램은 명령 줄 인수 n을 입력받아 두 가지 전략(선택을 바꾸거나 바꾸지 않거나)을 이용해 게임을 n번 실행하고 각 전략의 성공률을 출력해야 한다.
"""
import sys
import random


def dont_change_dec(n: int) -> float:
    cnt = 0
    for _ in range(n):
        doors = [1, 0, 0]
        cnt += random.choice(doors)

    return cnt / n


def change_dec(n: int) -> float:
    cnt = 0
    for _ in range(n):
        doors = [1, 0, 0]
        random.shuffle(doors)
        # first choice
        doors.pop()

        # show option
        if doors[0] == 1:
            doors.pop()
        else:
            doors.pop(0)

        # change choice
        cnt += doors.pop()

    return cnt / n


if __name__ == "__main__":
    n = int(sys.argv[1])
    dcd = dont_change_dec(n)
    cd = change_dec(n)

    print(f"don't change decison: {dcd * 100:.2f}%")
    print(f"change decison: {cd * 100:.2f}%")
