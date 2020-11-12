"""심화문제 23 - 극 좌표
직교 좌표를 극 좌표로 변환하는 프로그램을 작성하라.
프로그램은 두 개의 실수 x와 y를 명령 줄 인수로 입력받아 극좌표 r과 @를
출력해야 한다. y/x의 아크탄젠트 값(-ㅠ에서 ㅠ사이)을 계산하는 파이썬 함수
math.atan2(y, x)를 활용하라.
"""
import sys
import math

x = float(sys.argv[1])
y = float(sys.argv[2])

radian = math.atan2(y, x)
degree = radian * 180 / math.pi
print(f"radian: {radian}, degree: {degree}")
