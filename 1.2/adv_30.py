"""심화문제 30 - 대원(great circle, 구를 둘로 나눴을 때 생길 수 있는 가장 큰 원)
지구 위의 2개의 점위 위도와 경도를 도 단위로 표현한 네 개의 실수 x1, y1, x2, y2를 명령줄 인수로 받아
두 점 간의 대원 거리를 출력하는 프로그램을 작성하라
"""
import sys
import math

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

x1 = math.degrees(x1)
y1 = math.degrees(y1)
x2 = math.degrees(x2)
y2 = math.degrees(y2)

d = 60 * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
print(f"d: {d}")
