import statistics

# Functions Part 2

# With documentation and type hinting (optional)

# def my_fuction(country: str = 'Norway') -> None:
#     ''' I am explaning what my country does 

#     -country parameter with default value'''
#     print("I am from", country)

# my_fuction("Sweden") #It's gonna override the default.
# my_fuction("Brazil")
# my_fuction()


# or 

# def my_fuction(country: str = 'Norway') -> None:
#     return country

# my_fuction("Sweden") #It's gonna override the default.
# my_fuction("Brazil")
# my_fuction()
'''
Exercise
Write a function called center that returns either the mean or median of a list of numbers.
This function should take two parameters: A list of numbers, and an optional parameter called use_median which should default to False.
If use_median is False, return the mean of the list.
If use_median is True, return the median of the list.
Test your function by calling it with different arguments.
'''

'''No documentation or type hinting'''
# def center(my_list,use_median= False):
#     if use_median == False:
#         return statistics.mean(my_list)
#     else:
#         return statistics.median(my_list)

test_list1 = [1,2,2,2,3,4,5,6,7,8]
test_list2 = [3,6,7,9,10,11,2]

# result = center(test_list1,True)
# print(result)

# or
# my_median = center(test_list1,True)
# my_mean = center(test_list1)
# my_mean_two = center(test_list1,False)
# print(my_median)
# print(my_mean)
# print(my_mean_two)






'''Documentation, type hinting, shorthand if-then-else'''

def center(my_list:list,use_median:bool = False) -> float:
    '''Return either mean or median of a list of numbers
    -my list : the list to extract mean or median
    -use_median: bool to select mean or median'''
    return statistics.mean(my_list) if use_median == False else statistics.median(my_list)
test_list1 = [1,2,2,2,3,4,5,6,7,8]
test_list2 = [3,6,7,9,10,11,2]


# same  way 
    # if use_median == False:
    #     return statistics.mean(my_list)
    # else:
    #     return statistics.median(my_list)

# my_median = center(test_list1,True)
# my_mean = center(test_list1)
# my_mean_two = center(test_list1,False)
# print(my_median)
# print(my_mean)
# print(my_mean_two)






# Returning multiple values

def get_vowels_and_consonants(word):
    vowels = ''
    consonants = ''
    for letter in word:
        if letter in 'aeiou':
            vowels += letter
        elif letter in 'bcdfghjklmnpqrstvwxyz':
            consonants += letter
    return vowels, consonants

# vowels, consonants = get_vowels_and_consonants("apple")

# print(vowels)
# print(consonants)


'''
Exercise
Write a Python function called get_stats that takes in a list of numbers and returns the following three values: The mean, the median, and the mode of the list.
Call the function on a list, and print each statistic on a separate line.
my_list = [1,2,4,5,5]
Output:
Mean: 3.4
Median: 4
Mode: 5
'''

my_list = [1,2,4,5,5]

# def get_stats(my_list:list)-> str:
#     my_mean = statistics.mean(my_list)
#     my_median = statistics.median(my_list)
#     my_mode = statistics.mode(my_list)
#     return f'Mean: {my_mean}\nMedian: {my_median}\nMode: {my_mode}'
# # you can return a formated string 

# print(get_stats(my_list)) # This is a function call, or invocation



'''Global variables'''

# x = 'challenging'
# def change_x():
#     x = 'fun'

# change_x()  # function call 
# print("Programming is", x)


# x = 'challenging'
# def change_x():
#     global x
#     x = 'fun'
    
# change_x()
# print("Programming is", x)

'''
A lambda is a small anonymous function. It can take any number of arguments, but it can only have one expression, which is returned.
Syntax: lambda arguments : expression
'''

# Function to add two numbers
# def add_two(x,y):
#     return x + y
# print(add_two(5,7))

add_two = lambda x,y: x + y 
# print(add_two(5,7))
# print((add_two)(5,8))

# Written as a Lambda



# Write the following functions as Lambdas

def greeting(fname):
    print(f'Hello, {fname}')

fname = 'Daniel'
lname = 'Smith'
# lambda fname,lname  :f'Hello,{fname} {lname}'
# print((lambda fname,lname:f'Hello,{fname} {lname}')(fname,lname))
               
# def double_me(num):
#     return num + num

# print(double_me(20)) # function call ,within a print statement 


# def double_me(num):
#     return num +num 
# double_me = lambda num: num + num 

# print(double_me(4))

'''
Exercise
Write a lambda that computes the n-th power of a number, given two arguments, num and n.
Now, write a function that is equivalent to the lambda.
'''

# def power(num,n):
#     return num ** n
# power = lambda num, n : num ** n 
# print(power(2,6))




''' Higher Order Functions
These are functions that may accept a function as an argument or return a function as its output. In Python, reduce(), map() and filter() are some of the most important higher-order functions. When combined with simpler functions, they can be used to execute complex operations.

filter - The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not. 

map - returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

'''
# Let's use the filter function to find the even numbers in a list
def even_function(n):
    return n % 2 == 0 
n = 6 
# print(even_function(n))
# Apply Filter to find even number 
my_list = [0,1,2,3,4,5,6,7,8,9,10]

# even_num_filter = filter(lambda n :n % 2 == 0 ,my_list)
# print(list(even_num_filter))


# Triple Me! Triple the numbers in this lsit

triple_me = [0,1,2,3,4,5,6]

# result = map(lambda n: n * 4, triple_me)
# print(list(result))





# Lambda with sort

students = [{"name":"Kim","grade":98},
            {"name":"Joe","grade":65},
            {"name":"Ted","grade":93},
            {"name":"Keisha","grade":80},
            {"name":"Torrie","grade":65},
            {"name":"Simon","grade":78}]

# students_by_name = sorted(students, key = lambda s: s['name'],reverse=reversed)
 
# print(students_by_name)

# students_by_grade = sorted(students,key=lambda s: s['grade'],reverse=reversed)
# print(students_by_grade)

'''
Assignment 6
Write a simple function that returns a person's net worth. Here are your requirements:
Docstring which includes what function does and information on your parameters (brief)
Function name - net_worth
parameters - assets, liabilities
Must contain type hinting for the parameters as well as what the function will be returning
Call the function in a print statement with needed arguments
'''

# def net_worth(assets:float,liabilities:float) -> float:
#     "'Return networth -user's assets -user's liabilities'"
#     return assets - liabilities

# print(net_worth(20000,100000))






