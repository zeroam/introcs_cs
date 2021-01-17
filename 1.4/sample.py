"""프로그램 1.4.1 - 교환하는 대신 샘플 추출하기
m - 샘플 크기
n - 범위
perm[] - 0부터 n - 1 사이의 조합
"""
import random
import sys
import stdarray
import stdio

m = int(sys.argv[1])
n = int(sys.argv[2])

# 배열 초기화
perm = stdarray.create1D(n, 0)
for i in range(n):
    perm[i] = i

# perm[0...m]에 m개의 무작위 샘플을 생성
for i in range(m):
    r = random.randint(i, n - 1)

    # swap
    temp = perm[r]
    perm[r] = perm[i]
    perm[i] = temp

# 결과 출력
for i in range(m):
    stdio.write(str(perm[i]) + " ")
stdio.writeln()
