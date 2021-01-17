"""프로그램 1.4.4 - 자기 회피 무작위 보행
중복된 구간을 지나지 않고 주어진 크기의 격자를 빠져나올 수 있는 확률
"""
import random
import sys
import stdarray
import stdio

n = int(sys.argv[1])
trials = int(sys.argv[2])
deadEnds = 0

for i in range(trials):
    a = stdarray.create2D(n, n, False)
    x = n // 2
    y = n // 2
    while (x > 0) and (x < n - 1) and (y > 0) and (y < n - 1):
        # 궁지에 몰렸는 지 확인하고 나서 무작위로 다음 길을 선택한다.
        a[x][y] = True
        if a[x - 1][y] and a[x + 1][y] and a[x][y - 1] and a[x][y + 1]:
            deadEnds += 1
            break
        r = random.randrange(1, 5)
        if r == 1 and not a[x + 1][y]:
            x += 1
        if r == 2 and not a[x - 1][y]:
            x -= 1
        if r == 3 and not a[x][y + 1]:
            y += 1
        if r == 4 and not a[x][y - 1]:
            y -= 1

stdio.writeln(f"{100 * deadEnds // trials}% 궁지에 몰림")
