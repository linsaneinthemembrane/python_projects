"""Prints all instances of Friday the 13th in a given year."""

from datetime import datetime

year = int(input("Input a valid year: "))

for month in range(1, 13):
    date = datetime(year, month, 13)
    
    if date.weekday() == 4:
        # Print the date in the format mm/dd/yyyy
        print(date.strftime("%m/%d/%Y"))