import sys
import stdio

year = int(sys.argv[1])

# 4로 나누어지면 윤년
is_leap_year = (year % 4 == 0)
# 4로 나누어지되 100으로 나누어지면 윤년이 아님
is_leap_year = is_leap_year and ((year % 100) != 0)
# 100으로 나누어지되 400으로 나누어지면 윤년
is_leap_year = is_leap_year or ((year % 400) == 0)

stdio.writeln(is_leap_year)
