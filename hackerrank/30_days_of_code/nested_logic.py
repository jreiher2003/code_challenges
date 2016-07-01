def nest_logic(day1,month1,year1,day2,month2,year2):
    if year1 < year2: 
        return 0
    if year1 == year2 and month1 < month2:
        return 0
    if year1 == year2 and month1 == month2 and day1 <= day2: 
        return 0
    if year1 == year2 and month1 == month2 and day1 > day2:
        return (day1 - day2)*15
    if year1 == year2 and month1 > month2:
        return (month1 -month2)*500
    if year1 > year2:
        return (year1-year2)*10000 

print nested(9,6,2015,6,6,2015)

