from datetime import date
import holidays

us_holidays = holidays.PL()  # this is a dict
# the below is the same, but takes a string:
us_holidays1 = holidays.country_holidays('US')  # this is a dict



print (date(2024, 3, 31) in us_holidays)
