
# name = input("What is your name? ")

# num_age = int(input("How old are you? "))

# num_apple = int(input("How many apples do you eat in a day? "))

# life_span = int((num_age * num_apple) * 0.7)

# # comment = f"Hi {name}, You have {life_span} years more longer to live"


# '''     BELOW OR 2 OTHER WAYS OF OUTPUTTING THE RESULTS ON THE CONSOLE

# comment = "Hi {}, You have {} years more longer to live".format(name, life_span)

# '''


# '''
# comment = "Hi %, You have % years more longer to live" %name %life_span

# '''
# comment = "Hi %s You have %s years more longer to live" %(name, life_span)

# print(comment)  


name = input("What is your name")
principle = int(input("Enter principle amount: "))
rate = 0.07
number_of_times = int(input("Enter the number of times interest is compounded in in year: "))
time = int(input("Enter time(years): "))

Amount = principle * (1 + (rate/number_of_times))**(number_of_times * time)

print(f"Amount is {(Amount//10) * (10)} ")