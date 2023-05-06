"""
word = "Samuel"

surname = 'Ochefije'
name1 = "Muel " + str(surname)
name2 = "Sam " + str(surname)
name3 = "Male " + str(surname)

print(name1)
print(name2)
print(name3)
"""

import random

def childrenNames(nameOfFather, childrenAge):
    childrenNames = []

first_name, last_name = nameOfFather.split(' ')

for age in childrenAge:
    kidName = ''
    
    if age > len(first_name):
        first_name = first_name + first_name[:len(first_name)//2]

        for _ in range (age):
            kidName += random.choice(first_name)

            kidFullName = kidName.capitalize() + ' ' + last_name
            childrenNames.append(kidFullName)
        
        return childrenNames
    
print(childrenNames("Adikwu Samuel", [4, 6]))
