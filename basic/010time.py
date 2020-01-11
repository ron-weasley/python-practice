import time, datetime
from datetime import datetime, date, timedelta
from time import sleep

dt = date.today() - timedelta(5)
print("Current Date :", date.today())
print("5 days before Current Date :", dt)
print(datetime.fromtimestamp(int("1284105682")).strftime("%Y-%m-%d %H:%M:%S"))

start = time.time()
for i in ["1", "2", "3"]:
    print("{0} : {1}".format(i, "lol"))
    sleep(0.05)
end = time.time()
print(end - start)

date_object = datetime.strptime("Jul 1 2014 2:43PM", "%b %d %Y %I:%M%p")
print(date_object)
print(date_object.__format__("%b"))
