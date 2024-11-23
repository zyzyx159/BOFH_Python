from datetime import datetime
import calendar
import time

dateString = "Fri 22 Nov 2024 // 09:25 UTC"

dt_object = datetime.strptime(dateString, "%a %d %b %Y // %H:%M %Z")

timeStamp = calendar.timegm(dt_object.utctimetuple())

print("Unix time: " + str(timeStamp))
formattedTime = time.strftime('%Y-%m-%d %H:%M', time.gmtime(timeStamp))
print("Human time: " + formattedTime)