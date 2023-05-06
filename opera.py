#Addition
x = 10
y = 5
print(x + y)

#Substraction
x = 10
y = 5
print(x - y)

#Multiplication
x = 10
y = 5
print(x * y)

#Division
x = 10
y = 5
print(x / y)

#Modulus
x = 10
y = 3
print(x % y)

#Exponentiation
x = 5
y = 5
print(x ** y) #5*5*5*5*5

#Floor division
x = 15
y = 2
print(x // y) #the floor division // rounds the result down to the nearest whole number


#ASSIGNMENT OPERATORS
x = 5
print(x)

x = 10
x += 3
print(x)

x = 10
x -= 3
print(x)

x = 10
x *= 3
print(x)

x = 10
x /= 2
print(x)

x = 10
x %= 3
print(x)

x = 10
x //= 3
print(x)

x = 10
x **= 3
print(x)

x = 10
x &= 3
print(x)

x = 10
x |= 3
print(x)

x = 10
x ^= 3
print(x)

x = 10
x >>= 3
print(x)

x = 10
x <<= 3
print(x)


#COMPARISON OPERATORS
a = 10
b = 5
print(a == b)   # Output: False

a = 10
b = 5
print(a != b)   # Output: True

a = 10
b = 5
print(a > b)    # Output: True

a = 10
b = 5
print(a < b)    # Output: False

a = 10
b = 5
print(a >= b)   # Output: True

a = 10
b = 5
print(a <= b)   # Output: False


#LOGICAL OPERATORS
a = 10
b = 5
c = 7
print(a > b and a > c)   # Output: True

a = 10
b = 5
c = 7
print(a > b or a < c)    # Output: True

a = 10
b = 5
c = 7
print(not(a > b and a > c))  # Output: False


#BITWISE OPERATORS
a = 10    # 1010
b = 5     # 0101
print(a & b)   # Output: 0 (0000)

a = 10    # 1010
b = 5     # 0101
print(a | b)   # Output: 15 (1111)

a = 10    # 1010
b = 5     # 0101
print(a ^ b)   # Output: 15 (1111)

a = 10    # 1010
b = 5     # 0101
print(~a)      # Output: -11 (-1011)

a = 10    # 1010
b = 5     # 0101
print(a << 1)  # Output: 20 (10100)

a = 10    # 1010
b = 5     # 0101
print(a >> 1)  # Output: 5 (0101)


#MEMBERSHIP OPERATORS
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)   # Output: True

my_list = [1, 2, 3, 4, 5]
print(6 in my_list)   # Output: False

my_tuple = ('apple', 'banana', 'orange')
print('apple' not in my_tuple)   # Output: False

my_tuple = ('apple', 'banana', 'orange')
print('grape' not in my_tuple)   # Output: True

