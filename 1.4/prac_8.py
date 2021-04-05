"""연습문제 8
명령 줄 인수로 n을 입력받고 뒤섞은 카드에서 n명에게 카드를 돌렸을 때(각기 카드 5장)의
카드 패를 빈 줄로 구분해 출력하는 deal.py 프로그램을 작성하라.
"""
import sys
import random


def make_deck():
    cards = []
    nums = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    marks = ["♠︎", "♣︎", "♥︎", "♦︎"]

    for mark in marks:
        for num in nums:
            cards.append(f"{mark} {num}")

    random.shuffle(cards)

    return cards


n = int(sys.argv[1])
if n > 8:
    print("maximum people is 8!")
    sys.exit(1)

deck = make_deck()
print(deck)
for _ in range(n):
    print([deck.pop(random.randrange(len(deck))) for _ in range(5)])
