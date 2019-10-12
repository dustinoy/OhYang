def centuryFromYear(year):
    if 1<=year<=2005 and year%100==0:
        return int(year/100)
    else:
        return int(year/100)+1
