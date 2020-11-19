"""심화문제 25 - 정렬 확인
명령 줄 인수로 세 개의 실수 x, y, z를 입력받아 이 숫자들이 오름차순 (x < y < z)이나
내림차순 (x > y > z)으로 정렬되어 있으면 True, 아니면 False를 출력하는 프로그램을
작성하라.
"""
import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

if x < y < z or x > y > z:
    print("True")
else:
    print("False")
