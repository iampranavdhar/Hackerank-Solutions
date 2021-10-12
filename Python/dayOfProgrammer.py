def checkYear(year):
    if(year<=1917):
        if(year%4) == 0:
            return True
        else:
            return False
    else:
        if(year>=1919):
            if (year % 4) == 0:
                if (year % 100) == 0:
                    if (year % 400) == 0:
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False

year = int(input())
is_leap = False
month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
is_leap = checkYear(year)
if(year == 1918):
    month_days[1]= 15 #Here first 14 days are not considered
if(is_leap):
    month_days[1] = 29
summ = 0
month = 0
for i in range(len(month_days)):
    summ = summ + month_days[i]
    if(summ+month_days[i+1]>256):
        month = i+2
        break
remaining = 256 - summ
print(f"{remaining}.{month:02}.{year}")


