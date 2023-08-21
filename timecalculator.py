# time_calculator.py
def add_time(start, duration, day=None):
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    if period == 'PM':
        start_hour += 12
    
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute
    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60

    if new_hour < 12:
        new_period = 'AM'
    else:
        new_period = 'PM'
        new_hour %= 12
    
    if new_hour == 0:
        new_hour = 12
    
    days_later = total_minutes // (24 * 60)

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day:
        day = day.capitalize()
        start_day_index = days_of_week.index(day)
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        result = f"{new_hour}:{new_minute:02d} {new_period}, {new_day}"
    else:
        result = f"{new_hour}:{new_minute:02d} {new_period}"
    
    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"
    
    return result


# main.py
from time_calculator import add_time
from unittest import main

print(add_time("11:06 PM", "2:02"))

main(module='test_module', exit=False)


# test_module.py
import unittest
from time_calculator import add_time

class UnitTests(unittest.TestCase):
    # ... (rest of the test cases)

  if __name__ == "__main__":
    unittest.main()
