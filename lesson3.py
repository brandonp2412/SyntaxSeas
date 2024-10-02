# Lesson 3 - Mathematics

hours = 24
days = 7
months = 12
year = 365

# Calculate how many hours are in a week

week = 0
for i in range(0, days):
    week += hours
print('There are:', week, 'hours in a week (loop)')

# How can we simplify this?

print('There are:', days * hours, 'hours in a week (multiplication)')

# How many weeks are there in a year?

print('There are:', year / days, 'weeks in a year (division)')

# Let's shorten that number...

print('There are:', year // days, 'weeks in a year (floor)')