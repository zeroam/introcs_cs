"""프로그램 1.4.2 - 카드 수집가 시뮬레이션
카드 하나를 무작위로 뽑았을 때 모든 종류의 카드를 보기까지 뽑아야 하는 카드의 갯수 카운팅
"""
import random
import sys
import stdarray
import stdio

n = int(sys.argv[1])

count = 0
collectedCount = 0
isCollected = stdarray.create1D(n, False)  # 체크용 배열 사용

while collectedCount < n:
    # create random card
    value = random.randrange(0, n)
    count += 1
    if not isCollected[value]:
        collectedCount += 1
        isCollected[value] = True

stdio.writeln(count)
