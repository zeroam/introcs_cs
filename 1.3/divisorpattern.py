"""1.3.4 - 처음 접하는 내포된 루프"""
import sys
import stdio

n = int(sys.argv[1])

for i in range(1, n + 1):
    # i번째 줄을 출력한다.
    for j in range(1, n + 1):
        # i번째 줄에서 j번째 항목을 출력한다.
        if (i % j == 0) or (j % i == 0):
            stdio.write("* ")
        else:
            stdio.write("  ")
    stdio.writeln(i)
