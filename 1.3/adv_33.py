"""심화학습 33 - 체크섬(checksum)
국제 표준 도서 번호(ISBN)는 책을 식별하는 10자리 고유한 숫자이다.
오른쪽 끝에 있는 숫자는 체크섬으로서 나머지 숫자 9개에 의해 결정되며
d1 + 2*d2 + 3*d3 + 4*d4 + ... + 10*d10 이 11의 배수가 되는 성질을 갖고 있다.
ex) 020131452X -> X = 5
9자리 정수를 명령 줄 인수로 입력받아 체크섬을 계산하고 ISBN 번호를 출력하는 프로그램을 작성하라.
"""
import sys

nums = sys.argv[1]

if len(nums) != 9:
    print("Enter 9 numbers")
    sys.exit(1)

total = 0
for i, num in enumerate(nums):
    total += (i + 1) * int(num)

for i in range(10):
    x = i
    temp_total = total + x * 10
    if temp_total % 11 == 0:
        break
else:
    print("No valid number")
    sys.exit(1)

print(f"ISBN: {nums + str(x)}, checksum: {x}")
