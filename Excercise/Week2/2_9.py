def is_leap(year):
    return ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

def day_of_year(day, month, year):
  day_of_month = [(1, 31), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]
  day_index = 0

  # Check if enter 29 Feb on not leap year
  if day == 29 and month == 2 and not is_leap(year):
      return -1

  # check if user enter day 31th on 30 days month 
  if not (day <= day_of_month[month - 1][1]):
      return -1

  for i in range(0, month - 1):
      if i != 1:
          day_index += day_of_month[i][1]
      elif i == 1:
          day_index += 29 if is_leap(year) else 28

  day_index += day

  return day_index

def day_in_year(year):
    pass

def date_diff(date1, date2):
    how_many_day_between = 0
    start_day, start_month, start_year = [int(num) for num in date1.split('-')]
    stop_day, stop_month, stop_year = [int(num) for num in date2.split('-')]

    # ! Return -1 if the month is invalid
    if start_month > 12 or stop_month > 12 or start_month < 1 or stop_month < 1:
        return -1
  
    # ! Return -1 if input date is invalid
    if day_of_year(start_day, start_month, start_year) == -1 or day_of_year(stop_day, stop_month, stop_year) == -1:
        print('ERR1')
        return -1

    # ! Return -1 if start date come after stop date (You cannot calculate the future to past !!)
    if stop_year < start_year or (start_year == stop_year and start_month > stop_month) or (start_year == stop_year and start_month == stop_month and start_day > stop_day):
        print("ERR2")
        return -1


    # If the two input dates are in the same year, return the different between their day_of_year() function
    if start_year == stop_year:
        return day_of_year(stop_day, stop_month, stop_year) - day_of_year(start_day, start_month, start_year) + 1

    # I dont know what is these shit doing
    for i in range(start_year, stop_year+1):
        if i != start_year and i != stop_year:
            how_many_day_between += (366 if is_leap(i) else 365)
        elif i == start_year:
            how_many_day_between += (366 if is_leap(i) else 365) - day_of_year(start_day, start_month, start_year) + 1
        elif i == stop_year:
            how_many_day_between += day_of_year(stop_day, stop_month, stop_year)

    return how_many_day_between