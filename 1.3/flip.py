"""1.3.1 동전 던지기"""
import random
import stdio

if random.randrange(0, 2) == 0:
    stdio.writeln("앞")
else:
    stdio.writeln("뒤")
