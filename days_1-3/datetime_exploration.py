from datetime import datetime
from datetime import date

# returns todays date
datetime.today()

today = datetime.today()
# datetime object- important because you cant mix these objects
type(today)

todaydate = date.today()
todaydate

# note that when using date, the object type is a date and note a datetime
type(todaydate)

todaydate.month
todaydate.year
todaydate.day

# assigning the date to a variable
christmas = date(2022, 12, 5)

# can see that the type is automatically a timedelta 
christmas - todaydate

# using the days attribute of the datetime class returns an integer
(christmas - todaydate).days

if christmas != today:
    print(f'its not christmas yet! there are still {(christmas - todaydate).days} days left')
else:
    print('yay its christmas')