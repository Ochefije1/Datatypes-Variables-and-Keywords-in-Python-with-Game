


# '''
# In Python, a list is a collection of ordered, mutable, 
# and heterogeneous elements. Lists are defined using 
# square brackets [] and elements are separated by commas.

# my_list = [1, 2, "three", 4.0, True]


# In this example, my_list is a list that contains five elements of different types - an integer (1), another integer (2), a string ("three"), a float (4.0), and a boolean (True).

# You can access the elements of a list using indexing, where the first element has an index of 0. Here is an example:


# print(my_list[0])  # Output: 1
# print(my_list[2])  # Output: three

# You can also modify the elements of a list using indexing, since lists are mutable. Here is an example:

# my_list[3] = 3.5
# print(my_list)  # Output: [1, 2, "three", 3.5, True]



# Python lists also support a number of built-in methods for manipulating the contents of the list, such as append(), remove(), and sort().

# '''



# # carts = list()
# # carts = []

# # carts = [(1, 2, 3), [2, 3], 3, 4, 'apple', 5]

# # i = carts.index('apple')

# # cart = ['banana', 'guava']
# # carts.extend(cart)

# # carts.insert(i, 'orange')

# # print(i, carts)




# import time
# import random

# items_list = ['books', 'purse', 'laptop', 'shirts', 'pants', 'brush']
# eaten = []

# while len(items_list) > 0:
#     index = random.randint(0, len(items_list) -1)
#     eaten_item = items_list.pop(index)
#     time.sleep(4)
#     print(f'{eaten_item} is eaten')
#     eaten.append(eaten_item)





fruits = ['apple', 'orange', 'banana', 'coconut']

# print(fruits[:3])
# print(fruits[::2])


# for fruit in fruits:
#     print(fruit) 
#     print(len(fruits))
#     print('pineapple' in fruits)


# # print(help(fruits))
# # print(dir(fruit))



fruits.append('paw-paw')
fruits.remove('coconut')
fruits.insert(0, 'pear')

fruits[1] = 'pineapple'
fruits.sort()
fruits.index('orange')
fruits.reverse()
fruits.clear()

for fruit in fruits:
    print(fruit)