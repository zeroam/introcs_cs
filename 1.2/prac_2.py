"""연습문제 2
명령 줄 인수로 입력받은 모든 @에 대해 cos^2@ + sin^2@가 대략 1.0이 되는지 확인하는 프로그램을
math.sin()과 math.cos()을 이용해 작성하라. 계산된 값이 늘 1.0이 되지 않는 이유는 무엇일까?
"""
import sys
import math
import stdio

theta = int(sys.argv[1])

result = math.cos(theta) ** 2 + math.sin(theta) ** 2
stdio.writeln(result)
