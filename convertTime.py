from datetime import datetime
import pytz

#website string
dateString = "Fri 22 Nov 2024 // 09:25 UTC"

importFormat = ("%a %d %b %Y // %H:%M %Z")
dt = datetime.strptime(dateString, importFormat)
dtWithTZ = dt.replace(tzinfo=pytz.utc)

outputDate = ("%Y-%m-%d")
    #2024-11-22
outputDateTime = ("%A, %B %d %Y at %H:%M %Z")
    #Friday, November 22 2024 at 09:25 UTC
adjustTimeZone = dtWithTZ.astimezone(pytz.timezone('US/Central'))
    #Friday, November 22 2024 at 03:25 CST

reAdjTime = dtWithTZ.astimezone(pytz.timezone('US/Central')).strftime("%A, %B %d %Y at %H:%M %Z")

# print(dtWithTZ.strftime(outputDate))
# print(dtWithTZ.strftime(outputDateTime))
# print(adjustTimeZone.strftime(outputDateTime))
# print(dtWithTZ)
# print(dtWithTZ.strftime("%Z"))
print(reAdjTime)