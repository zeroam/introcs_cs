"""연습문제 7
for 루프 한 개와 if 조건문 한 개를 이용해 1000(포함)에서 2000(미포함)까지를
정수를 한 줄에 5개씩 출력하는 fiveperline.py 프로그램을 작성하라.
"""
for i in range(1000, 2000):
    if i % 5 != 4:
        print(i, end=", ")
    else:
        print(i)
print()
