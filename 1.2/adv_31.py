"""심화문제 31 - 세 숫자 정렬
명령 줄 인수로 세 개의 정수를 입력받아 오름차순으로 출력하는 프로그램을 작성하라
"""
import sys

nums = list(map(int, sys.argv[1:4]))
print(sorted(nums))
