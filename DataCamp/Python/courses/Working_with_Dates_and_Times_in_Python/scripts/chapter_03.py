# exercise 01

"""
Creating timezone aware datetimes

In this exercise, you will practice setting timezones manually.
"""

# steps

"""

    Import timezone.
    Set the tzinfo to UTC, without using timedelta.
---

    Set pst to be a timezone set for UTC-8.
    Set dt's timezone to be pst.
---

    Set aedt to be a timezone set for UTC+11.
    Set dt's timezone to be aedt.

"""

# solution

# Import datetime, timezone
from datetime import datetime, timezone

# October 1, 2017 at 15:26:26, UTC
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=timezone.utc)

# Print results
print(dt.isoformat())

#----------------------------------#

# Import datetime, timedelta, timezone
from datetime import datetime, timedelta, timezone

# Create a timezone for Pacific Standard Time, or UTC-8
pst = timezone(timedelta(hours=-8))

# October 1, 2017 at 15:26:26, UTC-8
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=pst)

# Print results
print(dt.isoformat())

#----------------------------------#

# Import datetime, timedelta, timezone
from datetime import datetime, timedelta, timezone

# Create a timezone for Australian Eastern Daylight Time, or UTC+11
aedt = timezone(timedelta(hours=11))

# October 1, 2017 at 15:26:26, UTC+11
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=aedt)

# Print results
print(dt.isoformat())

#----------------------------------#

# exercise 02

"""
Setting timezones

Now that you have the hang of setting timezones one at a time, let's look at setting them for the first ten trips that W20529 took.

timezone and timedelta have already been imported. Make the change using .replace()
"""

# steps

"""

    Create edt, a timezone object whose UTC offset is -4 hours.
    Within the for loop:
    Set the tzinfo for trip['start'].
    Set the tzinfo for trip['end'].

"""

# solution

# Create a timezone object corresponding to UTC-4
edt = timezone(timedelta(hours=-4))

# Loop over trips, updating the start and end datetimes to be in UTC-4
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo=edt)
  trip['end'] = trip['end'].replace(tzinfo=edt)

#----------------------------------#

# exercise 03

"""
What time did the bike leave in UTC?

Having set the timezone for the first ten rides that W20529 took, let's see what time the bike left in UTC. We've already loaded the results of the previous exercise into memory.
"""

# steps

"""
Within the for loop, move dt to be in UTC. Use timezone.utc as a convenient shortcut for UTC.
"""

# solution

# Loop over the trips
for trip in onebike_datetimes[:10]:
  # Pull out the start
  dt = trip['start']
  # Move dt to be in UTC
  dt = dt.astimezone(timezone.utc)
  
  # Print the start time in UTC
  print('Original:', trip['start'], '| UTC:', dt.isoformat())

#----------------------------------#

# exercise 04

"""
Putting the bike trips into the right time zone

Instead of setting the timezones for W20529 by hand, let's assign them to their IANA timezone: 'America/New_York'. Since we know their political jurisdiction, we don't need to look up their UTC offset. Python will do that for us.
"""

# steps

"""

    Import tz from dateutil.
    Assign et to be the timezone 'America/New_York'.
    Within the for loop, set start and end to have et as their timezone (use .replace()).

"""

# solution

# Import tz
from dateutil import tz

# Create a timezone object for Eastern Time
et = tz.gettz('America/New_York')

# Loop over trips, updating the datetimes to be in Eastern Time
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo = et)
  trip['end'] = trip['end'].replace(tzinfo = et)

#----------------------------------#

# exercise 05

"""
What time did the bike leave? (Global edition)

When you need to move a datetime from one timezone into another, use .astimezone() and tz. Often you will be moving things into UTC, but for fun let's try moving things from 'America/New_York' into a few different time zones.
"""

# steps

"""

    Set uk to be the timezone for the UK: 'Europe/London'.
    Change local to be in the uk timezone and assign it to notlocal.
---

    Set ist to be the timezone for India: 'Asia/Kolkata'.
    Change local to be in the ist timezone and assign it to notlocal.
---

    Set sm to be the timezone for Samoa: 'Pacific/Apia'.
    Change local to be in the sm timezone and assign it to notlocal.

"""

# solution

# Create the timezone object
uk = tz.gettz('Europe/London')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in the UK?
notlocal = local.astimezone(uk)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

#----------------------------------#

# Create the timezone object
ist = tz.gettz('Asia/Kolkata')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in India?
notlocal = local.astimezone(ist)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

#----------------------------------#

# Create the timezone object
sm = tz.gettz('Pacific/Apia')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in Samoa?
notlocal = local.astimezone(sm)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

#----------------------------------#

# exercise 06

"""
How many hours elapsed around daylight saving?

Since our bike data takes place in the fall, you'll have to do something else to learn about the start of daylight savings time.

Let's look at March 12, 2017, in the Eastern United States, when Daylight Saving kicked in at 2 AM.

If you create a datetime for midnight that night, and add 6 hours to it, how much time will have elapsed?
"""

# steps

"""
You already have a datetime called start, set for March 12, 2017 at midnight, set to the timezone 'America/New_York'.

Add six hours to start and assign it to end. Look at the UTC offset for the two results.
---
You added 6 hours, and got 6 AM, despite the fact that the clocks springing forward means only 5 hours would have actually elapsed!

Calculate the time between start and end. How much time does Python think has elapsed?
---
Move your datetime objects into UTC and calculate the elapsed time again.

Once you're in UTC, what result do you get?
"""

# solution

# Import datetime, timedelta, tz, timezone
from datetime import datetime, timedelta, timezone
from dateutil import tz

# Start on March 12, 2017, midnight, then add 6 hours
start = datetime(2017, 3, 12, tzinfo = tz.gettz('America/New_York'))
end = start + timedelta(hours=6)
print(start.isoformat() + " to " + end.isoformat())

#----------------------------------#

# Import datetime, timedelta, tz, timezone
from datetime import datetime, timedelta, timezone
from dateutil import tz

# Start on March 12, 2017, midnight, then add 6 hours
start = datetime(2017, 3, 12, tzinfo = tz.gettz('America/New_York'))
end = start + timedelta(hours=6)
print(start.isoformat() + " to " + end.isoformat())

# How many hours have elapsed?
print((end - start).seconds/(60*60))

#----------------------------------#

# Import datetime, timedelta, tz, timezone
from datetime import datetime, timedelta, timezone
from dateutil import tz

# Start on March 12, 2017, midnight, then add 6 hours
start = datetime(2017, 3, 12, tzinfo = tz.gettz('America/New_York'))
end = start + timedelta(hours=6)
print(start.isoformat() + " to " + end.isoformat())

# How many hours have elapsed?
print((end - start).total_seconds()/(60*60))

# What if we move to UTC?
print((end.astimezone(tz.UTC) - start.astimezone(tz.UTC))\
      .total_seconds()/(60*60))

#----------------------------------#

# exercise 07

"""
March 29, throughout a decade

Daylight Saving rules are complicated: they're different in different places, they change over time, and they usually start on a Sunday (and so they move around the calendar).

For example, in the United Kingdom, as of the time this lesson was written, Daylight Saving begins on the last Sunday in March. Let's look at the UTC offset for March 29, at midnight, for the years 2000 to 2010.
"""

# steps

"""

    Using tz, set the timezone for dt to be 'Europe/London'.
    Within the for loop:
    Use the .replace() method to change the year for dt to be y.
    Call .isoformat() on the result to observe the results.

"""

# solution

# Import datetime and tz
from datetime import datetime
from dateutil import tz

# Create starting date
dt = datetime(2000, 3, 29, tzinfo = tz.gettz('Europe/London'))

# Loop over the dates, replacing the year, and print the ISO timestamp
for y in range(2000, 2011):
  print(dt.replace(year=y).isoformat())

#----------------------------------#

# exercise 08

"""
Finding ambiguous datetimes

At the end of lesson 2, we saw something anomalous in our bike trip duration data. Let's see if we can identify what the problem might be.

The data is loaded as onebike_datetimes, and tz has already been imported from dateutil.
"""

# steps

"""
Loop over the trips in onebike_datetimes:

    Print any rides whose start is ambiguous.
    Print any rides whose end is ambiguous.
"""

# solution

# Loop over trips
for trip in onebike_datetimes:
  # Rides with ambiguous start
  if tz.datetime_ambiguous(trip['start']):
    print("Ambiguous start at " + str(trip['start']))
  # Rides with ambiguous end
  if tz.datetime_ambiguous(trip['end']):
    print("Ambiguous end at " + str(trip['end']))

#----------------------------------#

# exercise 09

"""
Cleaning daylight saving data with fold

As we've just discovered, there is a ride in our data set which is being messed up by a Daylight Savings shift. Let's clean up the data set so we actually have a correct minimum ride length. We can use the fact that we know the end of the ride happened after the beginning to fix up the duration messed up by the shift out of Daylight Savings.

Since Python does not handle tz.enfold() when doing arithmetic, we must put our datetime objects into UTC, where ambiguities have been resolved.

onebike_datetimes is already loaded and in the right timezone. tz and timezone have been imported. Use tz.UTC for the timezone.
"""

# steps

"""

    Complete the if statement to be true only when a ride's start comes after its end.
    When start is after end, call tz.enfold() on the end so you know it refers to the one after the daylight savings time change.
    After the if statement, convert the start and end to UTC so you can make a proper comparison.

"""

# solution

trip_durations = []
for trip in onebike_datetimes:
  # When the start is later than the end, set the fold to be 1
  if trip['start'] > trip['end']:
    trip['end'] = tz.enfold(trip['end'])
  # Convert to UTC
  start = trip['start'].astimezone(tz.UTC)
  end = trip['end'].astimezone(tz.UTC)

  # Subtract the difference
  trip_length_seconds = (end-start).total_seconds()
  trip_durations.append(trip_length_seconds)

# Take the shortest trip duration
print("Shortest trip: " + str(min(trip_durations)))

#----------------------------------#

# exercise 10

"""

"""

# steps

"""

"""

# solution



#----------------------------------#

# exercise 11

"""

"""

# steps

"""

"""

# solution



#----------------------------------#