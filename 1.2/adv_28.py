"""심화문제 28 - 메르카토르 도법
메르카토르 도법은 등각 투영법으로서, 위도(lat)와 경도(lon)를 직교 좌표(x, y)에 대응시킨다.
메르카토르 도법은 항해도나 웹에서 보는 지도에 널리 사용된다. 메르카토르 도법에서 
x = lat - lat0, y = 1/2 ln((1 + sin(lon)) / (1 - sin(lon))) 로 정의된다.
이때 lat0는 지도 중점의 위도이다.
lat0, 위도, 경도를 명령 줄 인수로 입력받아 직교 좌표 위의 점의 위치를 출력하는 프로그램을 작성하라.
"""
import sys
import math

lat0 = float(sys.argv[1])
lat = float(sys.argv[2])
lon = float(sys.argv[3])

x = lat - lat0
y = 1 / 2 * math.log((1 + math.sin(lon)) / (1 - math.sin(lon))) 

print(f"x: {x}, y: {y}")
