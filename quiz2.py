people = ['Megan', 'Brandon', 'John']
ages = [21, 26, 30]

# What names will be printed?
for person in people:
    print('Found person:', person)
    
# What ages will be printed?
for age in ages:
    print('Found age:', age)
    
# What does ages look like now?
ages.append(18)
print(ages)

# What will this output?
for index in range(0 , len(people)):
    print('Person:', people[index], 'is', ages[index], sep='\t')