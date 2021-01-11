"""심화학습 40 - 피프스의 문제
1693년 새뮤얼 피프스는 아이작 뉴턴에게 주사위를 공평히 6번 굴려서 1이 한 번 이상 나올 확률과
12번 굴려서 1이 두 번 이상 확률 중 어느 것이 더 노ㅠ은지 물었다.
뉴턴에게 간단히 답을 해줄 수 있는 프로그램을 작성하라.
"""
import random


def dice6() -> int:
    for _ in range(6):
        if random.randint(1, 6) == 1:
            return 1
    return 0


def dice12():
    cnt = 0
    for _ in range(12):
        if random.randint(1, 6) == 1:
            cnt += 1

    if cnt >= 2:
        return 1

    return 0


def calc_dice(dice_func, simulation: int) -> float:
    cnt = 0
    for _ in range(simulation):
        cnt += dice_func()

    return cnt / simulation


if __name__ == "__main__":
    simulation = 100000
    perc_6 = calc_dice(dice6, simulation)
    perc_12 = calc_dice(dice12, simulation)

    print(f"dice 6: {perc_6 * 100:.2f}%")
    print(f"dice 12: {perc_12 * 100:.2f}%")
