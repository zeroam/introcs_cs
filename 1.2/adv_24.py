"""심화문제 24 - 가우스 난수
다음의 박스-뮬러(Box-Muller) 공식을 이용하면 정규 분포에 따르는 난수를 생성할 수 있다.
    w = sin(2 ㅠ v)(-2 ln u)^(1/2)
이때 u와 v는 math.random() 함수로 생성한 0과 1사이의 실수이다.
표준 가우스 난수를 출력하는 프로그램을 작성하라.
"""
import math
import random

# 정규분포를 따르는 난수 생성
w = math.sin(2 * math.pi * random.random()) * (-2 * math.log(random.random())) ** (1/2)
print(f"정규분포 난수: {w}")

# 생성된 난수로 히스토그램 그리기
results = []
for i in range(100000):
    results.append(math.sin(2 * math.pi * random.random()) * (-2 * math.log(random.random())) ** (1/2))

import matplotlib.pyplot as plt
plt.hist(results, bins=1000)
plt.show()
