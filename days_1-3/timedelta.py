from datetime import date, datetime
from datetime import timedelta

# creating a timedelta object
t = timedelta(days=4, hours=10)

# returning the type - its a timedelta
type(t)

# this returns the correct number of days
t.days
# notice this is capped at 36 - the seconds can only go up to a maximum of 1 day
t.seconds

# this is dividing the seconds by 60 (for minutes) and 60 again (for hours)
t.seconds / 60 / 60

# this is doing the same thing
t.seconds / 60**2

eta = timedelta(hours=6)
today = datetime.today()

# timedeltas can just be added directly to a datetime object
# converting to str formats it nicely
str(today + eta)

