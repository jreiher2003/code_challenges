a = [int(a) for a in raw_input().split()]

import calendar  
b = []
for i in a:
    b.append(i)
    

year = b[2]
month = b[0]
day = b[1]

day_index = calendar.weekday(year, month, day)
#print day_index
#print list(calendar.day_name)
print list(calendar.day_name)[day_index].upper()