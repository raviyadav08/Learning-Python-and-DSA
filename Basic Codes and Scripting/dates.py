import os
import datetime
import pytz

os.chdir('C:/Users/iamsu/Desktop/Demo/Files')

dt = datetime.datetime.now(tz=pytz.UTC)
print(dt)


# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

