# Write a program time.py, which reads a number of seconds (an integer) and then prints the same amount of time given in hours,
#  minutes and seconds. An example of an execution:
# Give a number of seconds: 9999
# This corresponds to: 2 hours, 46 minutes and 39 seconds.

seconds_in_hour = 3600
seconds_in_minute = 60

seconds = int(input("Give a number of seconds: "))


hours = seconds // seconds_in_hour
seconds = seconds - (hours * seconds_in_hour)

minutes = seconds // seconds_in_minute
seconds = seconds - (minutes * seconds_in_minute)

print("This corresponds to:"" {0:.0f} hours, {1:.0f} minutes, {2:.0f} seconds.".format(
    hours, minutes, seconds))