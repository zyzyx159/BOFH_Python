from datetime import datetime
import calendar
import time
import pytz

#website string
dateString = "Fri 22 Nov 2024 // 09:25 UTC"

#human format
dt_object = datetime.strptime(dateString, "%a %d %b %Y // %H:%M %Z")

#date time
timeStamp = calendar.timegm(dt_object.utctimetuple())

#just date
formattedTime = time.strftime('%Y-%m-%d', time.gmtime(timeStamp))

centralTZ = pytz.timezone('US/Central')
eastTZ = pytz.timezone('US/Eastern')

print("human format: " + str(dt_object))
print("date time: " + str(timeStamp))
print("just date:" + str(formattedTime))