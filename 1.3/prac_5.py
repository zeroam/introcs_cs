"""연습문제 5
다음 각 코드 조각을 실행한 후의 j값은?
"""
j = 0
for i in range(j, 10):
    j += i
print(f"a. {j}")

j = 0
for i in range(10):
    j += i
print(f"b. {j}")

for j in range(10):
    j += j
print(f"c. {j}")
