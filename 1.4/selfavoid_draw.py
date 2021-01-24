"""프로그램 1.4.4 - 자기 회피 무작위 보행
중복된 구간을 지나지 않고 주어진 크기의 격자를 빠져나올 수 있는 확률
"""
import random
import sys
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.function_base import linspace
import stdarray
import stdio


def trim_axs(axs, N):
    """
    Reduce *axs* to *N* Axes. All further Axes are removed from the figure.
    """
    axs = axs.flat
    for ax in axs[N:]:
        ax.remove()
    return axs[:N]


n = int(sys.argv[1])
rows = int(sys.argv[2])
cols = int(sys.argv[3])
trials = rows * cols
deadEnds = 0

cases = []
for i in range(trials):
    x = n // 2
    y = n // 2
    xs, ys = [x], [y]

    a = stdarray.create2D(n, n, False)
    dead_end = False
    while (x > 0) and (x < n - 1) and (y > 0) and (y < n - 1):
        # 궁지에 몰렸는 지 확인하고 나서 무작위로 다음 길을 선택한다.
        a[x][y] = True
        if a[x - 1][y] and a[x + 1][y] and a[x][y - 1] and a[x][y + 1]:
            deadEnds += 1
            dead_end = True
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

        xs.append(x)
        ys.append(y)

    xs.append(x)
    ys.append(y)
    cases.append((xs, ys, dead_end))

stdio.writeln(f"{100 * deadEnds // trials}% 궁지에 몰림")


figsize = (10, 10)
axs = plt.figure(figsize=figsize, constrained_layout=True).subplots(rows, cols)
axs = trim_axs(axs, len(cases))
for ax, (xs, ys, dead_end) in zip(axs, cases):
    # set color
    if dead_end:
        color = "r"
    else:
        color = "b"

    ax.set_xlim((0, n - 1))
    ax.set_xticks(np.arange(0, n, 1))
    ax.set_xticklabels([])

    ax.set_ylim((0, n - 1))
    ax.set_yticks(np.arange(0, n, 1))
    ax.set_yticklabels([])

    ax.grid(True)

    ax.plot(xs[0], ys[0], color="black", marker="o")
    ax.plot(xs, ys, color=color, lw=2)

plt.show()
