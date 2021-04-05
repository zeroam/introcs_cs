"""연습문제 6
다음의 코드 조각은 어떤 값을 출력하는가?
"""
import stdarray
import stdio

a = stdarray.create1D(10, 0)
for i in range(10):
    a[i] = 9 - i
for i in range(10):
    a[i] = a[a[i]]
for v in a:
    stdio.writeln(v)
