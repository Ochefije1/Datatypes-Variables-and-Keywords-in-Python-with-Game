#even numbers
#odd numbers
#for each of the number raise it to the power highest number then divid it by sum of the total number and convert it to an integer, if it is even say it and if it is odd say it.

def evaluate():
    nums = range(num)
    sm = sum(nums)
    for num in nums:
        result = int((num ** max(nums))/sm)
        if result % 2 == 0:
            print('{} is even number' .format(result))
        else:
            print('%s is odd number' %result)


