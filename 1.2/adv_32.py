"""심화문제 32 - 용 곡선
0에서 5차까지의 용 곡선을 그리는 명령을 출력하는 프로그램을 작성하라.
곡선 그리는 명령은 일련의 F, L, R 문자로 구성된다. F는 "1 단위 앞으로 나가며 선 그리기",
L은 "좌회전", R은 "우회전"을 의미한다.
n차 용 곡선은 긴 종이를 n번 반으로 접고 나서 접힌 부분을 직각으로 펼친 모습이다.
"""

dragon0 = "F"
nogard0 = "F"
dragon1 = dragon0 + "L" + nogard0
nogard1 = dragon0 + "R" + nogard0
dragon2 = dragon1 + "L" + nogard1
nogard2 = dragon1 + "R" + nogard1
dragon3 = dragon2 + "L" + nogard2
nogard3 = dragon2 + "R" + nogard2
dragon4 = dragon3 + "L" + nogard3
nogard4 = dragon3 + "R" + nogard3
dragon5 = dragon4 + "L" + nogard4

print(dragon0)
print(dragon1)
print(dragon2)
print(dragon3)
print(dragon4)
print(dragon5)
