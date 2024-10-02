# Lesson 3 - Mathematics

hours = 24
days = 7
months = 12

# Calculate how many hours are in a week

week = 0
for i in range(0, days):
    week += hours
print('There are:', week, 'hours in a week (loop)')

# How can we simplify this?

print('There are:', days * hours, 'hours in a week (multiplication)')