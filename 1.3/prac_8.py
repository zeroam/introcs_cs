"""연습문제 8
[연습문제 1.2.27]의 '균등 분포 난수'문제룰 범용화해 stats.py 프로그램을 작성하라. stats.py
는 명령 줄 인수로 정수 n을 입력 받고, random.random()을 이용해 0과 1사이의 균등 분포 난수 n
개를 생성한 후, 이 난수들의 평균값, 최솟값, 최댓값을 출력한다.
"""
import sys
import random

n = int(sys.argv[1])

nums = [random.random() for _ in range(n)]
print(f"평균: {sum(nums) / n}, 최솟값: {min(nums)}, 최댓값: {max(nums)}")
