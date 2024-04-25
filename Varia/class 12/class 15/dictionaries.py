from statistics import mode

''' Fun facts about dictionaries 

    -collection of keys and values
    -used to store associated information
    -keys are the words, values are the definitions

'''

# How do we create a dictionary?

user_data = {"user id":400, "name": "Fritz","address":'1515 Mockingbird Lane'}

# print(user_data)
# print(type(user_data))


# Access keys with brackets
# print(user_data["name"])
# print(user_data['user id'])
# print(user_data['address'])

# # Add new key value
# user_data['state'] = 'NY'
# print(user_data['state'])
# user_data['state'] = 'NJ'
# print(user_data['state'])

# # lets look at all the methods available to us
# print(dir(user_data))

# # lets try one
# print(user_data.__contains__("user id"))
# print(user_data.__contains__("city"))

# Dict constructor


# Dictionary methods


dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Lets use the keys methods to get the keys from this dictionary
# Assign keys to a variable

# dog_information = dog.keys()
# print(dog_information)
# print(dog.keys())

# Lets use clear method to remove all elements

# dog.clear()
# print(dog)

# Lets use get method to get a key value

# age = dog.get('age')
# print(age)
# # # lets look at one of the parameters to show an error if the key doesnt exist

# print(dog.get('temperament','Key does not exist'))

# Lets create a copy
new_dog = dog.copy()

# print(new_dog)
# print(type(new_dog))


# Lets remove a specified key with pop
# new_dog.pop('breed')
# print(new_dog)


# Lets remove a last inserted key-value pair with popitem
# new_dog.popitem()
# print(new_dog)

# Get a list with each key-value pair with items, will return a list of tuples
key_value_pairs_in_a_list_of_tuples = new_dog.items()
print(key_value_pairs_in_a_list_of_tuples)


# we can loop through,using the items method 
for k, v in new_dog.items():
    print(k,v)


dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Update allows us to update by changing and adding data
dog.update({"temperament":"happy","breed":"chihuahua"})
print(dog)

# Dictionaries vs Lists
list1 = ['a', 'b', 'c', 'd', 'e']
dict1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 5: 'e'}
 
print(list1[3])
print(dict1[3])

list1[3] = 'z'
dict1[3] = 'z'

print(list1)
print(dict1)


'''
Write some code that takes two lists and converts them into one dictionary.
In:
list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]
Out:
{'one': 4, 'two': 10, 'three': 30}

'''

# Hint, both of these lists happen to have the same length
list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]



my_keys = ['one', 'two', 'three']
my_values = [4, 10, 30]

# Using Zip & Dict
# my_dictionary = dict(zip(my_keys,my_values))
# print(my_dictionary)

# Using dictionary comprehension
my_dictionary = {keys: values for (keys,values) in zip(my_keys,my_values)}
print(my_dictionary)


'''
Exercise

Write a dictionary that contains five words and their definitions. Then have your code print the word and their definition one at a time.
Hint: Use the items() method

'''

words = {"color":"blue", "veggie":"radish", "vehicle": "bike", "mood": "happy", "pet":"cat"}
print(words.items())

for w,c in words.items():
    print(w,c)


# As datasets, we can use bracket notation

choices = {"flavors":['strawberry', 'vanilla', 'orange'],
           "sizes":['large', 'medium', 'small']}

# print(choices['flavors'][0])
# print(choices['sizes'][2])


'''
Exercise
Create a dictionary for an automobile including make, model, year, number of doors, and number of cylinders.
'''

cars = {"make": "Honda","model":"Acoord","Year":2013,"number of doors":4,"cylinders": 6}


# print(cars.items())


'''
In statistics, the mode is the value that appears most frequently in a dataset.
For example, in this list: [1,2,4,1,3,4,1,1] the mode is 1
Write some code that uses a dictionary to calculate the mode of a list.

'''

my_list_items = [1,2,4,1,3,4,1,1,1,1,1,1,1,1,1,1,10,10,10,10] # our list


output = {} # my final output

# for m in my_list_items:
#     if m not in output:
#         output[m] = 1 # add it initially
#         # print(output)
#     else:
#         output[m] += 1 # updating the count 
# print(output) 

#  shorten the syntax 
# for m in my_list_items: # looping through the list 
#     output[m] = my_list_items.count[m]
# print(output)


# Statistics module
use_states_module = [1,2,4,1,3,4,1,10,10,10,10]
result = mode(use_states_module)
print(result)


# Looping through and adding 
incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}



'''
Suppose you have a list of employee records that contain the following information for each employee: name, job title, salary. The records are stored as a list of dictionaries.
Use this list to create a dictionary where the keys are the job titles and the values are the average salaries for each job title.
Example:
records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000}]
Output: {'manager': 50000, 'developer': 62500}
'''

records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000},
           {'name': 'Alice', 'title': 'consultant', 'salary': 25000},\
           {'name': 'David', 'title': 'consultant', 'salary': 40000}]









 



