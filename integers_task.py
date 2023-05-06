

def evaluate(num):
    nums = range(num)
    sm = sum(nums)
    for num in nums:
        result = int((num ** max(nums)) / sm)
        if result % 2 == 0:
            print(f'{result} is an even number')
        else:
            print(f'{result} is an odd number')

print(evaluate(10))




