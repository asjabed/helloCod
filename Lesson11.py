"""
Date Time module
-----------------
"""
from datetime import *

cdate= datetime.now()
print(cdate)
print (cdate.year)
print (cdate.month)
print (cdate.day)

print (cdate.hour)
print (cdate.minute)
print (cdate.second)

# formating Date and time
print(cdate.strftime("Week day short    :%a "))
print(cdate.strftime("Week day full     :%A "))
print(cdate.strftime("Week day number   :%w "))
print('='*80)

print(cdate.strftime("Day of month   :%d "))
print(cdate.strftime("Month short    :%b "))
print(cdate.strftime("Month full     :%B ")) 
print(cdate.strftime("Month number   :%m "))
print(cdate.strftime("Year without century   :%y "))
print(cdate.strftime("Year with century      :%Y "))
print('='*80)

print(cdate.strftime("Hour 24      :%H "))
print(cdate.strftime("Hour 12      :%I "))
print(cdate.strftime("Hour am/pm   :%p "))
print(cdate.strftime("Minute 60    :%M "))
print(cdate.strftime("Secoend 60   :%S "))
print(cdate.strftime("MicroSecoend :%f "))
print('='*80)

print(cdate.strftime("Full time :%T "))
print(cdate.strftime("Full date :%D "))

print(cdate.strftime("Custom time  :%I:%M:%S %p "))
print(cdate.strftime("Custom Date  :%Y-%m-%d "))
print(cdate.strftime("Custom Day  :%A,%B %d,%Y "))


