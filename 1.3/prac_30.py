"""연습문제 30
break 문을 사용하지 않고 단위 원판 위에 무작위로 분산된 점을 생성하는 프로그램을 작성하라.
여러분이 작성한 코드와 이번 절에서 설명한 코드를 비교하라.
-> 현재 구현한 코드는 균등하게 분산된 점이 아님
"""
import random
import math
import numpy as np
import matplotlib.pyplot as plt


def get_dir() -> int:
    """절반의 확률로 각각 1, -1 리턴"""
    n = random.random()
    if n < 0.5:
        return -1
    return 1


def create_point_me(r: int):
    x = get_dir() * random.random() * r
    y = get_dir() * random.random() * math.sqrt(r ** 2 - x * x)
    return (x, y)


def create_point(r: int) -> tuple:
    while True:
        x = get_dir() * random.random() * r
        y = get_dir() * random.random() * r
        if x * x + y * y <= r * r:
            break

    return (x, y)


repeat = 10000
r = 50

points = []
x = []
y = []
for _ in range(repeat):
    # 무작위 좌표 생성 (x^2 + y^2 <= r^2, -r <= x <= r)
    temp_x, temp_y = create_point(r)
    x.append(temp_x)
    y.append(temp_y)

# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005


rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom + height + spacing, width, 0.2]
rect_histy = [left + width + spacing, bottom, 0.2, height]

# start with a square Figure
fig = plt.figure(figsize=(8, 8))

ax = fig.add_axes(rect_scatter)
ax.set_xlim((-r - 2, r + 2))
ax.set_ylim((-r - 2, r + 2))
ax.grid(True)
ax_histx = fig.add_axes(rect_histx, sharex=ax)
ax_histy = fig.add_axes(rect_histy, sharey=ax)

# draw circle
circle = plt.Circle((0, 0), r)
ax.add_artist(circle)

# draw points
ax.scatter(x, y, color='black', zorder=2, s=5)

# now determine nice limits by hand:
binwidth = 1
xymax = max(max(x), max(y))
lim = (int(xymax/binwidth) + 1) * binwidth

bins = np.arange(-lim, lim + binwidth, binwidth)
ax_histx.hist(x, bins=bins)
ax_histy.hist(y, bins=bins, orientation='horizontal')


fig.savefig("prac_30.png")
