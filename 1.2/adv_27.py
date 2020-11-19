"""심화문제 27 - 균등 분포 난수
0.0과 1.0 사이의 균등 분포 난수 5개를 생성해 평균, 최솟값, 최댓값을 출력하는
프로그램을 작성하라. 내장된 min()과 max() 함수를 사용하라.
"""
import random

nums = [random.random() for _ in range(5)]
print(f"평균: {sum(nums) / 5}, 최솟값: {min(nums)}, 최댓값: {max(nums)}")
