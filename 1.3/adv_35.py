"""심화문제 35 - 2차원 무작위 행보
2차원 무작위 행보는 격자를 따라 이동하는 입자의 행위를 시뮬레이션한다.
각 단계별로 무작위 행보자는 이전의 이동과는 무관하게 동서남북을 모두 동일한 1/4의 확률로 이동한다.
명령 줄에서 정수 n을 인수로 입력받아 중점에서 시작한 행보자가 2n x 2n의 경계선에 도달하기까지의 이동 횟수를 예측하는
프로그램 randomwalker.py를 작성하라
"""
import sys
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = int(sys.argv[1])

x_points = [0]
y_points = [0]

x, y = 0, 0
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
ends = [n, -n]
while not (x in ends or y in ends):
    x_dir, y_dir = random.choice(directions)
    x += x_dir
    y += y_dir

    x_points.append(x)
    y_points.append(y)

    if x in ends or y in ends:
        break

print(f"moving: {len(x_points)}")


# draw
fig, ax = plt.subplots()
ax.set_xlim((-1 * (n + 1), (n + 1)))
ax.set_ylim((-1 * (n + 1), (n + 1)))
ax.grid(True)
(line,) = ax.plot([], [], lw=3)

# draw square
rect = plt.Rectangle((-n, -n), 2 * n, 2 * n, fc="none", ec="black", lw=2)
ax.add_patch(rect)


def init():
    line.set_data([], [])
    return (line,)


def animate(i):
    line.set_data(x_points[:i + 1], y_points[:i + 1])


anim = animation.FuncAnimation(
    fig, animate, frames=len(x_points), init_func=init, interval=100
)
anim.save("adv_35.gif", writer="imagemagick")
# plt.show()
