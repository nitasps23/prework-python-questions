# Prework-assignments -- Python Questions

# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
# The first line of the code has been defined as below.

#     def hello_name(user_name):
#         .....

def hello_name(user_name):
    """Print a simple hello to each user."""
    for name in user_name:
        print(f"\tHello, {name.title()}!")

username = ['nita', 'laura']
print("Say hello to the users:\n")
hello_name(username)

print("\n")
               
# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

#     def first_odds():
#         .....

def first_odds():
    """Print the odd numbers from 1-100 and returns nothing."""
    num = 0
    while num < 100:
        num += 1
        if num % 2 == 0:
            continue
        print(num)

print("Printing the odd numbers from 1-100:\n")
first_odds()

print("\n")
               
# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.
# The first line of the code has been defined as below.

#     def max_num_in_list(a_list):
#         .....

def max_num_in_list(a_list):
    """Return the max number of a given list."""
    num_max = max(a_list)
    return num_max

num_list = [22, 55, 1999, 39]
print(f"The max number in this list {num_list} is {max_num_in_list(num_list)} ")

print("\n")


# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

#     def is_leap_year(a_year):
#         .....

def is_leap_year(a_year):
    """Return if the given year is a leap year."""
    if a_year % 4 == 0 and a_year % 100 != 0 and a_year % 400 == 0:
        return False
    if a_year % 4 == 0 and a_year % 100 != 0:
        return True
    else:
        return False

enter_a_year = 2023
print(f"Check if {enter_a_year} is leap year: {is_leap_year(enter_a_year)}")


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

#     def is_consecutive(a_list):
#         .....

def is_consecutive(a_list):
    """Return if all numbers in list are consecutive numbers."""
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

num_list = [5, 9, 7, 8, 9]
print(f"\nCheck if all number in this list {num_list} are consecutive numbers: {is_consecutive(num_list)}")