
# '''
# NO 1
# In a basket of fruit, chek if a particular fruit is there.

# '''

# # note that this is an array method
# basket_of_fruits = ['soursop', 'udara', 'paw-paw', 'mango', 'tangerine']
# fruit = 'udara'

# if fruit in basket_of_fruits:
#     print(f"There is {fruit} in the basket of fruits")
# else:
#     print(f"There is no {fruit} in the basket of fruits")




'''
NO 2

For a word, count the number of vowels.
'''

def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for alpha in word:
        if alpha in vowels:
            count += 1
    return count

print(count_vowels('umbrella'))