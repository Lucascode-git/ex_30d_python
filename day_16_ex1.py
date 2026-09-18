from datetime import date, datetime

now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
min = now.minute
timest = now.timestamp()

print(day, month, year, hour, min, timest)
print()

formated = now.strftime('%m/%d/%Y, %H:%M:%S')
print(f'current date: {formated}')
print()

today = '5 December, 2019'
totime = datetime.strptime(today, '%d %B, %Y')
nexform = totime.strftime('%m/%d/%Y')
print(f'{today} -> become -> {nexform}')
print()

newyear = date(year=2027, month=1, day=1,)
now = datetime.now()
d = now.day
m = now.month
y = now.year
h = now.hour
mi = now.minute
s = now.second
nowyear = date(year=y, month=m, day=d)
diff = newyear - nowyear
print(diff)
print()

newyear = datetime(year=2027, month=1, day=1, hour=0, minute=0, second=0)
nowyear = datetime(year=y, month=m, day=d, hour= h, minute=mi, second=s)
stayday = newyear - nowyear
print(stayday)
print()

timest = now.timestamp()
minval = timest/60
hourval = minval/60
dayvalue = hourval/24

print(f'seconds : {int(timest)} OR minutes: {minval:.2f} OR hours: {hourval:.2f} OR days: {dayvalue:.2f}')
print('OR')
start_timestamp = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0)
nowyear = datetime(year=y, month=m, day=d, hour= h, minute=mi, second=s)
stayday =  nowyear - start_timestamp
print(stayday)
print()