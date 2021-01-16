"""심화학습 42. 무질서
인구 성장에 대한 다음의 단순 모델을 연구하는 프로그램을 작성하라.
t 시각에서의 개체 수가 x이면 t + 1 시각에서의 개체 수는 rx(1 - x)라고 가정한다.
r 값이 얼마일 때 x = 1 - 1/r 에서 개체 수가 안정화 되는가?
ex) r = 3.5, 3.8, 5
- 2 ~ 3일 때 안정적
"""
import sys
import matplotlib.pyplot as plt

r = float(sys.argv[1])

t = 100

x = 0.01
x_values = [x]

for _ in range(t):
    x = r * x * (1 - x)
    x_values.append(x)

plt.plot(x_values)
plt.show()
