# exercise 01

"""
Which day of the week?

Hurricane Andrew, which hit Florida on August 24, 1992, was one of the costliest and deadliest hurricanes in US history. Which day of the week did it make landfall?

Let's walk through all of the steps to figure this out.
"""

# steps

"""
Import date from datetime.
---
Create a date object for August 24, 1992.
---
Now ask Python what day of the week Hurricane Andrew hit (remember that Python counts days of the week starting from Monday as 0, Tuesday as 1, and so on).
"""

# solution

# Import date from datetime
from datetime import date

#----------------------------------#

# Import date from datetime
from datetime import date

# Create a date object
hurricane_andrew = date(1992,8,24)

#----------------------------------#

# Import date from datetime
from datetime import date

# Create a date object
hurricane_andrew = date(1992, 8, 24)

# Which day of the week is the date?
print(hurricane_andrew.weekday())

#----------------------------------#

# exercise 02

"""
How many hurricanes come early?

In this chapter, you will work with a list of the hurricanes that made landfall in Florida from 1950 to 2017. There were 235 in total. Check out the variable florida_hurricane_dates, which has all of these dates.

Atlantic hurricane season officially begins on June 1. How many hurricanes since 1950 have made landfall in Florida before the official start of hurricane season?
"""

# steps

"""
Complete the for loop to iterate through florida_hurricane_dates.
Complete the if statement to increment the counter (early_hurricanes) if the hurricane made landfall before June.
"""

# solution

# Counter for how many before June 1
early_hurricanes = 0

# We loop over the dates
for hurricane in florida_hurricane_dates:
  # Check if the month is before June (month number 6)
  if hurricane.month < 6:
    early_hurricanes = early_hurricanes + 1
    
print(early_hurricanes)

#----------------------------------#

# exercise 03

"""
Subtracting dates

Python date objects let us treat calendar dates as something similar to numbers: we can compare them, sort them, add, and even subtract them. This lets us do math with dates in a way that would be a pain to do by hand.

The 2007 Florida hurricane season was one of the busiest on record, with 8 hurricanes in one year. The first one hit on May 9th, 2007, and the last one hit on December 13th, 2007. How many days elapsed between the first and last hurricane in 2007?
"""

# steps

"""
Import date from datetime.
Create a date object for May 9th, 2007, and assign it to the start variable.
Create a date object for December 13th, 2007, and assign it to the end variable.
Subtract start from end, to print the number of days in the resulting timedelta object.
"""

# solution

# Import date
from datetime import date

# Create a date object for May 9th, 2007
start = date(2007, 5, 9)

# Create a date object for December 13th, 2007
end = date(2007, 12, 13)

# Subtract the two dates and print the number of days
print((end - start).days)

#----------------------------------#

# exercise 04

"""
Counting events per calendar month

Hurricanes can make landfall in Florida throughout the year. As we've already discussed, some months are more hurricane-prone than others.

Using florida_hurricane_dates, let's see how hurricanes in Florida were distributed across months throughout the year.

We've created a dictionary called hurricanes_each_month to hold your counts and set the initial counts to zero. You will loop over the list of hurricanes, incrementing the correct month in hurricanes_each_month as you go, and then print the result.
"""

# steps

"""
Within the for loop:
Assign month to be the month of that hurricane.
Increment hurricanes_each_month for the relevant month by 1.
"""

# solution

# A dictionary to count hurricanes per calendar month
hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6:0,
		  				 7: 0, 8:0, 9:0, 10:0, 11:0, 12:0}

# Loop over all hurricanes
for hurricane in florida_hurricane_dates:
  # Pull out the month
  month = hurricane.month
  # Increment the count in your dictionary by one
  hurricanes_each_month[month] += 1
  
print(hurricanes_each_month)

#----------------------------------#

# exercise 05

"""
Putting a list of dates in order

Much like numbers and strings, date objects in Python can be put in order. Earlier dates come before later ones, and so we can sort a list of date objects from earliest to latest.

What if our Florida hurricane dates had been scrambled? We've gone ahead and shuffled them so they're in random order and saved the results as dates_scrambled. Your job is to put them back in chronological order, and then print the first and last dates from this sorted list.
"""

# steps

"""
Print the first and last dates in dates_scrambled.
---
Sort dates_scrambled using Python's built-in sorted() function, and save the results to dates_ordered.
Print the first and last dates in dates_ordered.
"""

# solution

# Print the first and last scrambled dates
print(dates_scrambled[0])
print(dates_scrambled[-1])

#----------------------------------#

# Print the first and last scrambled dates
print(dates_scrambled[0])
print(dates_scrambled[-1])

# Put the dates in order
dates_ordered = sorted(dates_scrambled)

# Print the first and last ordered dates
print(dates_ordered[0])
print(dates_ordered[-1])

#----------------------------------#

# exercise 06

"""
Printing dates in a friendly format

Because people may want to see dates in many different formats, Python comes with very flexible functions for turning date objects into strings.

Let's see what event was recorded first in the Florida hurricane data set. In this exercise, you will format the earliest date in the florida_hurricane_dates list in two ways so you can decide which one you want to use: either the ISO standard or the typical US style.
"""

# steps

"""
Assign the earliest date in florida_hurricane_dates to first_date.
Print first_date in the ISO standard. For example, December 1st, 2000 would be "2000-12-01".
Print first_date in the US style, using .strftime(). For example, December 1st, 2000 would be "12/1/2000".
"""

# solution

# Assign the earliest date to first_date
first_date = min(florida_hurricane_dates)

# Convert to ISO and US formats
iso = "Our earliest hurricane date: " + first_date.strftime('%Y-%m-%d')
us = "Our earliest hurricane date: " + first_date.strftime("%m/%d/%Y")

print("ISO: " + iso)
print("US: " + us)

#----------------------------------#

# exercise 07

"""
Representing dates in different ways

date objects in Python have a great number of ways they can be printed out as strings. In some cases, you want to know the date in a clear, language-agnostic format. In other cases, you want something which can fit into a paragraph and flow naturally.

Let's try printing out the same date, August 26, 1992 (the day that Hurricane Andrew made landfall in Florida), in a number of different ways, to practice using the .strftime() method.

A date object called andrew has already been created.
"""

# steps

"""
Print andrew in the format 'YYYY-MM'.
---
Print andrew in the format 'MONTH (YYYY)', using %B for the month's full name, which in this case will be August.
---
Print andrew in the format 'YYYY-DDD' (where DDD is the day of the year) using %j.
"""

# solution

# Import date
from datetime import date

# Create a date object
andrew = date(1992, 8, 26)

# Print the date in the format 'YYYY-MM'
print(andrew.strftime('%Y-%m'))

#----------------------------------#

# Import date
from datetime import date

# Create a date object
andrew = date(1992, 8, 26)

# Print the date in the format 'MONTH (YYYY)'
print(andrew.strftime('%B (%Y)'))

#----------------------------------#

# Import date
from datetime import date

# Create a date object
andrew = date(1992, 8, 26)

# Print the date in the format 'YYYY-DDD'
print(andrew.strftime('%Y-%j'))

#----------------------------------#