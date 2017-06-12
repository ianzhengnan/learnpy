
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)

# Jan => Month.Jan , 1
# Feb => Month.Feb , 2
# Mar => Month.Mar , 3
# Apr => Month.Apr , 4
# May => Month.May , 5
# Jun => Month.Jun , 6
# Jul => Month.Jul , 7
# Aug => Month.Aug , 8
# Sep => Month.Sep , 9
# Oct => Month.Oct , 10
# Nov => Month.Nov , 11
# Dec => Month.Dec , 12

# 自定义枚举类
@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

day1 = Weekday.Mon
print(day1)

print(Weekday.Tue)

print(Weekday['Tue'])

print(Weekday.Tue.value)
print(day1 == Weekday.Mon)

for name, member in Weekday.__members__.items():
	print(name, '=>', member)

# Sun => Weekday.Sun
# Mon => Weekday.Mon
# Tue => Weekday.Tue
# Wed => Weekday.Wed
# Thu => Weekday.Thu
# Fri => Weekday.Fri
# Sat => Weekday.Sat