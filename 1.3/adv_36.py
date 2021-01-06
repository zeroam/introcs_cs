"""심화문제 36 - 다섯 숫자의 중앙값
명령 줄 인수로 다섯 개의 서로 다른 정수를 입력받아 중앙값을 출력하는 프로그램을 작성하라.
보너스: 프로그램이 주어진 값들을 비교한 횟수가 7보다 작으면 보너스 점수를 준다.
"""
import sys

nums = list(map(int, sys.argv[1:]))

if len(nums) != 5:
    print(f"input length must be 5 not {len(nums)}")
    sys.exit(1)

nums.sort()
print(f"median: {nums[2]}")
