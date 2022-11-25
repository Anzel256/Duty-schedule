from datetime import date
import pandas as pd
import calendar
import holidays


today = date.today()
current_month = int(today.strftime("%m"))
current_year = int(today.strftime("%Y"))
num_days = calendar.monthrange(current_year, current_month)


a = date(current_year, current_month, 25)
print(a.strftime('%A'))
print (a)
pl_holidays = holidays.PL()
range_with_days = range(num_days[0], num_days[1]+1)
day = []
data = {}
is_holiday = []
day_of_the_week = []
for single_day in range_with_days:
    current_date = date(current_year, current_month, single_day)

    data[single_day] = ((current_date) in pl_holidays, current_date.strftime('%A'))
    
    day.append(current_date)
    is_holiday.append((current_date) in pl_holidays)
    day_of_the_week.append(current_date.strftime('%A'))




df = pd.DataFrame([data])
df.to_excel(r'C:\Users\Anzel\Projects\Schedule.xlsx', index=False)


list_of_tuples = list(zip(day,day_of_the_week, is_holiday))
df2 = pd.DataFrame(list_of_tuples,
                  columns=['Data','Dzień tygodnia', 'Święto'])
df2.to_excel(r'C:\Users\Anzel\Projects\Schedule2.xlsx', index=False)