def is_year_leap(year):
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

def days_in_month(year, month):
    if year < 0 or not (1 <= month < 12):
        return None
    
    days_per_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    if month == 2 and is_year_leap(year):
        return 29

    return days_per_month[month-1]
      
def day_of_year(year, month, day):
	sum_days = 0
	for i in range(month-1):
		sum_days += days_in_month(year, i+1)

	sum_days += day
	return sum_days


print(day_of_year(2000, 12, 31))

