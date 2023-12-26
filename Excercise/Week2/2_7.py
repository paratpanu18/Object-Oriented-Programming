def day_of_year(day, month, year):
    day_of_month = [(1, 31), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]
    day_index = 0

    print(is_leap(year))

    # Check if enter 29 Feb on not leap year
    if (day == 29) and (month == 2) and (not is_leap(year)):
        return "Incorrect date 1"

    # check if user enter day 31th on 30 days month 
    # if not (day <= day_of_month[month - 1][1]):
    #     return "Incorrect date 2"

    for i in range(month - 1):
        if i != 1:
            day_index += day_of_month[i][1]
        elif i == 1 and is_leap(year):
            day_index += 29
    
    day_index += day

    return day_index

def is_leap(year):
    return ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

day, month, year = [int(num) for num in input().split()]
print(day_of_year(day, month, year))
# print(is_leap(1904))