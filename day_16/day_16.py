#day 16 of 30 days with python
from datetime import datetime

#get current date
today = datetime.now()
print("Today's date:", today)

#Format date
date_t = today.strftime("%m/%d/%Y, %H:%M:%S")
print(date_t)

#change the time string to time
date_str= '5 December, 2019'
date_object = datetime.strptime(date_str, '%d %B, %Y')
print("Date object:", date_object)

# Calculate the difference from New Year
new_year = datetime(2020, 1, 1)
diff= new_year - date_object
print("Difference:", diff)

# Calculate the difference from a specific date
date_a= datetime(1970, 1, 1)
diff=today - date_a
print("Difference from 1970-01-01:", diff)