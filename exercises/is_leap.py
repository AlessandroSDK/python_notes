def is_leap(year):
    leap = False
    if year >= 100000:
        return "Number not > 100000"
    if year % 400 == 0:
        return True
    if  year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return leap

year = int(raw_input())
print is_leap(year)
