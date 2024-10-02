people = ['Megan', 'Brandon', 'John']
ages = [21, 26, 30]

# What names will be printed?
for person in people:
    print('Found person:', person)
    
# What ages will be printed?
for age in ages:
    print('Found age:', age)
    
ages.append(18)
print(ages)

# What does ages look like now?

for index in range(0 , len(people)):
    print('Person:' , people[index] , 'is' , ages[index],sep='\t')