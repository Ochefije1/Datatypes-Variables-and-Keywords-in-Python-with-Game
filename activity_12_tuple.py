#class1 = {'homan', 'Niyi', 'Niyi'}
#class2 = {'john', 'new_man', 'Niyi'}

#print()

from string import ascii_letters, punctuation, ascii_uppercase, ascii_lowercase

A = set('ABab12@45')
B = set('Ab1570&&')

#print(A.difference(B))

#print(A.symmetric_difference(B))

A.add(9)
B.discard('b')

print(A, B)


