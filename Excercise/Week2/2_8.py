def day_of_year(day, month, year):
    day_of_month = [(1, 31), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]
    day_index = 0

    # Check if enter 29 Feb on not leap year
    if day == 29 and month == 2 and not is_leap(year):
        return "Incorrect date"

    # check if user enter day 31th on 30 days month 
    if not (day <= day_of_month[month - 1][1]):
        return "Incorrect date"

    for i in range(month - 1):
        if i != 1:
            day_index += day_of_month[i][1]
        elif i == 1:
            day_index += 29 if is_leap(i) else 28
    
    day_index += day

    return day_index

def is_leap(year):
    return ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

def date_diff(date1, date2):
    how_many_day_between = 0
    start_day, start_month, start_year = [int(num) for num in date1.split('-')]
    stop_day, stop_month, stop_year = [int(num) for num in date2.split('-')]

    if start_year == stop_year:
        return day_of_year(stop_day, stop_month, stop_year) - day_of_year(start_day, start_month, start_year) + 1

    for i in range(start_year, stop_year+1):
        if i != start_year and i != stop_year:
            how_many_day_between += (366 if is_leap(i) else 365)
        elif i == start_year:
            how_many_day_between += (366 if is_leap(i) else 365) - day_of_year(start_day, start_month, start_year) +1
        elif i == stop_year:
            how_many_day_between += day_of_year(stop_day, stop_month, stop_year) 
        
    return how_many_day_between 

day_one , day_two = [str(i) for i in input().split()]
print(date_diff(day_one , day_two ))