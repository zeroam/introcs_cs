"""연습문제 6
useargument.py를 응용해 세 개의 이름을 명령 줄 인수로 입력받아 역순으로 출력하는
prac_6.py 프로그램을 작성하라. 예를 들어 python prac_6.py Alice Bob Carol 명령을 실행하면
Hi, Carol, Bob, and Alice 문장을 출력해야 한다.
"""
import sys
import stdio

stdio.write("Hi ")
stdio.writeln(f"{sys.argv[3]}, {sys.argv[2]}, {sys.argv[1]}")
