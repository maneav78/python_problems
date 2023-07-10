# The program has a month and a year of two dates. The user enters another date (month and year only). Determine if the third date ranges from the first date to the second, inclusive. Solve the problem using dict.

import calendar

date1 = {'month': 'May', 'year': 1980}
date2 = {'month': 'July', 'year': 2004}
date3 = {
    'month': input('Write the month: '),
    'year': input('Write the year: ')
}
data = dict(zip(list(calendar.month_name[1:]), range(1, 13)))
# (or like this) data = {month: index for index, month in enumerate(calendar.month_name) if month}

if(data[date1['month']] < data[date3['month']] < data[date2['month']] and date1['year'] < int(date3['year']) < date2['year']):
    print('True')
else:
    print('False')


