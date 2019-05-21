from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
date_br = now.strftime("%d%m%Y")

print("date and time:",date_time)
print("DATE BR: ", date_br)
print("NOW : ", now)

 
