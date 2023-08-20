#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the 
#input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    return(user_name + "!")

print(hello_name("hello_USERNAME"))
print("\n")

#Question2
#Write a python function, first_odds that prints the 
#odd numbers from 1-100 and returns nothing

def first_odds():
    F_o = list(range(1,101,2))    
    first_odds()
    print(F_o)

#Question3
#Please write a Python function, max_num_in_list to return the max
#number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """We will find out the max number in a list of numbers"""
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return(sum(a_list))
print(max_num_in_list('a_list'))
print("\n")

#Question4
#Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless 
# it is also divisible by 400. The return should be boolean Type 
# (true/false).


def is_leap_year(a_year):
    """We will find out if a year is leap year"""

User = input("Ask me a year, and I will tell you if it is a leap year: ")

a_year = int(User)
if a_year % 4 == 0:
    print("true")
else:
    print("false")
print("\n")

#Question5 
#Write a function to check to see if all numbers in list are
# consecutive numbers. For example, [2,3,4,5,6,7] are consecutive 
# numbers, but [1,2,4,5] are not consecutive numbers. The return
# should be boolean Type.

def is_consecutive(a_list): 
    """We're gonna see if our list is consecutive"""
a_list = []
x = 1
for num in range(1,11):
    con = num + x 
    a_list.append(con)

if a_list == [num + x for num in range(1,11)]:
    print("You did it! this is consecutive!")
else:
    print("Back to the drawing boards")
