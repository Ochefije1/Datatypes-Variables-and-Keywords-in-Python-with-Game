# # tupples are immutable

# month = ([1, 3, 4])

# # although tupples are immutable, but you can change/mutate the content of the tupple

# month[0][2] = month[0][2] * 2
# print(month)




# man = set()  #this is a way of defining an empty set, and sets are mutable


# man = {}    #this is called dictionary


# class1 = {'homan', 'Niyi', 'Niyi'}
# class2 = {'john', 'new_man', 'Niyi'}
# print(class1)



from string import ascii_letters, punctuation, ascii_uppercase, ascii_lowercase

letters_lower = set(ascii_lowercase)
letters = set(ascii_letters)

print(letters.difference(letters_lower))




A = set('ABab12@45')
B = set('Ab1570&&')

print(A.intersection(B))
print(A.union(B))
print(A.difference(B))
print(A.symmetric_difference(B))
A.add('9')
B.discard('b')
A.add('4')
print(A, B)