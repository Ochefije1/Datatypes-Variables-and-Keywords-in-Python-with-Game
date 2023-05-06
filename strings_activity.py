# name = 'house'

# print(type(name))


# print(name.center(8, '*'))

# print(name.center(100, '-'))

# print(name.istitle())

# print(name.isdigit())

# print(name.isalpha())


# namer = 'house for sale'
# print(namer.endswith('sale'))

# print(namer.translate(str.trans(97:101)))

# table = str.make


# nam = 'abracadabra'
# print(nam[-4:])

# print(nam[::-1])      #this is slicing methos. It reverses the word. re-writing it in the opposite direction

# print(nam.split(' '))

# nan = 'ab\nrac\nad'
# print(nan.splitlines())





# comment = "the red fox jumped over the lazy dog"
# #STEP 1:

# new = ''

# comment_arr = comment.split('') #['the' 'red' ... 'dog']

# for word in comment_arr:

# #     first_two_letters = word[:2].upper()

# #     rest_letters = word[2:]

# #     doubled_letter = ''

# #     for letter in rest_letters:
# #         doubled_letters += letter * 2

# #     new += first_two_letters + doubled_letter + ''

# # print(new)




#     word = word[:2].upper() + ''.join([letter * 2 for letter in word[2:]])

# print(new)



# this is to get names of children from the letters of my name, with my surname attatched 

import random

def childrenNames(nameOfFather, childrenAge):

    childrenNames = []

    first_name, last_name = nameOfFather.split(' ')

    for age in childrenAge:
        kidName = ''

        if age > len(first_name):
            first_name = first_name + first_name[:len(first_name)//2]

        for _ in range(age):
            kidName += random.choice(first_name)

        kidFullName = kidName.capitalize() + ' ' + last_name
        childrenNames.append(kidFullName)

    return childrenNames 

names_of_children = childrenNames("Wisdom Johnson", [8,6, 4,2])

print(names_of_children)

