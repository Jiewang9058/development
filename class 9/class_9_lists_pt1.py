''' Lists '''


# Indexing
planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter']


# Update with indexing
colors = ['red', 'green', 'yellow', 'blue', 'orange']



# Iterate with for loop
animals = ['dog', 'cat', 'lion', 'tiger', 'eagle']



# Len function gives us the amount of items in a list
modes_of_travel = ['car', 'plane', 'truck', 'train', 'boat']


'''
Exercise

Create a for loop that goes through a list and prints each item in the list, along with its index. (Hint: Create a separate counter variable to keep track of the index.)

Example:
planets = ["mercury", "venus", "earth", "mars"]
0: mercury, 1: venus, 2: earth, 3: mars

'''





''' Exercise
Write some code that takes one list and creates a second list that has the type for each entry in the list. Hint: Use the type() function and a for loop

Optional:
Make sure you filter out any repeats.

data = ['car', 3, True, False, 4.09, 'Tuesday']

'''
# Our collections


# Looping through for types



# Optional, remove repeats using sets


''' List Methods '''

'''
append() Adds an element at the end of the list
clear() Removes all the elements from the list
copy() Returns a copy of the list
count() Returns the number of elements with the specified value
extend() Add the elements of a list (or any iterable), to the end of the current list
index() Returns the index of the first element with the specified value
insert() Adds an element at the specified position
pop() Removes the element at the specified position
remove() Removes the first item with the specified value
reverse() Reverses the order of the list
sort() Sorts the list

'''

food = ['ice cream', 'pizza', 'apple', 'burger', 'cookies']

# lets add salad with append



# lets remove all items with clear



# let create a copy


# How many times does pizza appear?


# Lets add items of a list to our food list
vegetables = ['carrots', 'asparagus', 'broccoli']


# lets find the index value for apple
# food = ['ice cream', 'pizza', 'apple', 'burger', 'cookies']
# print(food.index("apple"))


# Lets add cereal to the 3rd spot in our list


# Lets remove a food by index position
#

# Lets remove an item with a specified value


# Lets reverse our list



# Lets sort our list


# Sort versus sorted()

# Sorted returns a newer sorted list




'''
Exercise: List of Pets

You want to make a list containing the types of pets that the user has. Keep prompting the user for a pet until they enter "stop". If it's a new pet, add it to the list. If the list already has that pet, don't add it.

'''

# user_input = '' # initialization 
# pet_name = [] # This will capture animal names 

# while user_input != 'stop' :
#     user_input = input ("Please enter your pets name: " )
#     if user_input == 'stop': #This is to not add stop to the list 
#         break
#     elif user_input not in pet_name:
#         pet_name.append(user_input)
#     else:
#         print(f'{user_input} is already in the list')

# print(pet_name)





# pet_list = ['dog','cat','rabbit','snak']
# input = ('Please select the pet')



''' Removing duplicates from a list, but leaving 1'''

colors = ['blue', 'blue', 'blue', 'green', 'red', 'blue', 'blue']

# Option 1 
# new_colors = [] # capture unique colors 
# for c in colors: # looping through original list 
#     if c not in new_colors:
#         new_colors.append(c)
# print(new_colors)


# Option 2 - Using Sets
# colors = list(set(colors))
# print(colors)


'''
Example: Removing Values
You have a list of numbers, but it contains multiple of the number 2. Remove the number 2 until it only appears in the list once.

num_values = [2, 3, 4, 3, 2, 2, 2, 4, 1, 3, 4, 5]
'''
num_values = [2, 3, 4, 3, 2, 2, 2, 4, 1, 3, 4, 5, 2, 2, 2, 2] # removes an item based on its value. If there are multiple, it removes the first item with that value.

num_values = [2, 3, 4, 3, 2, 2, 2, 4, 1, 3, 4, 5]
# Option 1
   new_numvalues = [] # capture unique colors 
   for n in num_values:
      if n not in new_numvalues:
         num_values.append(n)
   print(new_numvalues)



# Option 2





'''
You have a list storing important data for your company, but it contains some duplicate entries. Go through your list and remove all the duplicates. When you're done, each item should appear in the list exactly once.
Hint: How would you expand our previous example, which removed duplicates of one value, to remove duplicates of all values?
Hint 2: You might want to make a copy of the original list to use as reference. You may want to use more than one loop.

transaction_dates = []
'''

transaction_dates = ['3/5/2024', '3/5/2024', '5/4/2019', '2/23/2023', '5/4/2019','5/2/2023', '2/23/2023', '2/23/2024', '8/6/2019', '5/4/2019','3/5/2024','5/2/2023']




# Using sets

