"""연습문제 26
factors.py에서 루프 종료 조건 (i * i <= n)을 (i < n)으로 바꾸면 어떤 영향이 있는지 간단히 실험해보라.
두 경우에서 n을 변경해 가면서 10초 안에 실행을 완료할 수 있는 n의 최댓값을 찾아내라
"""
import sys
import stdio
import time

n = int(sys.argv[1])

start = time.time()
factor = 2
while factor < n:
    while (n % factor) == 0:
        # 소인수로 나눈 후 소인수를 출력한다.
        n //= factor
        stdio.write(str(factor) + " ")
    factor += 1

if n > 1:
    stdio.write(n)
stdio.writeln()

print(f"elapsed: {time.time() - start:.4f}s")
