from datetime import datetime
import datetime

'''
Classes
'''
# Class Definition and Initializer
class Point2d:
    ''' Initializier '''
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y 

    '''String Representation'''
    def __str__(self):
        return f'({self.x},{self.y})'
    
    #Add your object to another object of your class
    def __add__(self, other):
        return Point2d(self.x + other.x, self.y + other.y)
    
    # Subtract my object from another object 
    def __sub__(self, other):
        return Point2d(self.x - other.x, self.y - other.y)
    
    # Test equality between this object and another 
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    # Less than fuction 
    def __lt__(self,other):
        if self.x < other.x and self.y < other.y:
            return True
        return False
    
    # Mutator Method - Setter
    def set_x(self,new_x):
        self.x = new_x
    # Mutator method for y 
    def set_y(self,new_y):
        self.y = new_y

    # Accessor Method for x 
    def get_x(self):
        return self.x
    
    # Accessor method for y 
    
# creating objectS of the Point2D Class
# point1 = Point2d(4,10) 
# point2 = Point2d(5,9)



# Return a string representation of this object
# print(point1)
# print(point2)   
    
# Adds this object to another object from the same class, return a new object.
# print(point1 + point2)
    
# Subtracts another object from this object, return a new object.
# print(point1 - point2)

# Test equality between this object and another, return a boolean.
# point3 = Point2d(3,4)   
# point4 = Point2d(3,4)
# print(point3 == point4)


# #less than function 
# point5 = Point2d(10,12)
# point6 = Point2d(9,1)
# print(point5 < point6)

# # Mutator method

# point7 = Point2d(5,11)  
# point7.set_x(10) # our method will change the value of x 
# print(point7)

# point7.set_y(25)
# # print(point7)

# # Accessor method
# print(point7.get_x())


'''Exercise - Dog Class
This class will take 3 paremeters ,dog name ,dog breed,and age (human years ) '''


class Dog:

    def __init__(self,name, birth_year, breed):
        self.name = name
        self.birth_year = birth_year
        self.breed = breed

    
    def __str__(self):
        return f'{self.name} is a {self.breed} and was born in {self.birth_year}'
     
    def human_age(self):
        today = datetime.datetime.now()
        year = today.year
        return f'{self.name} is {year - self.birth_year} years old in human years '
        # return year - self.birth_year
 
    # Write a method that will calculate dog years 
    def dog_years(self):
        dog_years = 7 * self.human_age()
        return f'{self.name} is {dog_years} in dog years '
    # years old in dog years 

# dog1 = Dog('Fido',2020, 'Golden Retriever') # Created our first object of the dog class
# dog2 = Dog('Zuzu',2021,'Dachsund')
# dog3 = Dog('srella',2016,'Japanese Chin')

# string representation 
# print(dog1)
# print(dog2)
# print(dog3)

# Human age method
# print(dog1.human_age())
# print(dog2.human_age())
# print(dog3.human_age())

# Dog years method
# print(dog1.dog_years())
# print(dog2.dog_years())
# print(dog3.dog_years())


# today = datetime.datetime.now()
# year = today.year
# print(year)





# print(point7.get_x())
   

# Create a point object with attributes x=2, y=3

# Let’s add a __str__ method to our Point2D class so we can print Point2D objects.


# Lets add __add__ to add objects of the same class together


# Lets try __sub__ to add objects of the same class together

# Let's try __eq__ method to test equality
'''What is the output of this code if we don't override ==?
What is the output if we override == to use value equality?
Is it the same or different? Why?

Without the __eq__ method, we will only be able to test if it is the same object
'''



# Let's try __lt__ method to test less than


# Setting with mutator methods



# Getting with accessor methods





''' Exercise - Date Class
1.Display the date in a format of mm/dd/yyyy
2.compare 2 different dates, if they are equal
3.compare which date came first
4.determine if a date is a leap year 
 '''

class Date:

    def __init__(self, year=1970, month=1, day=1):
        '''These are our parameters'''
        self.year = year
        self.month = month
        self.day = day 
 # this will control what the print built in function displays 
    def __str__(self):
        return f'Month: {self.month:02d}\nDay: {self.day:02d}\nYear: {self.year}'

    def __eq__(self, other):
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        return False
  
  # creat a methon to handle less than date objects, which date came first?
    def __lt__(self,other):
        selfdate = datetime.datetime(self.year, self.month, self.day)
        otherdate = datetime.datetime(other.year, other.month, other.day)
        if selfdate < otherdate :
            return True
        return False
    
    def is__leap__year(self):
        if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0 ):
            return True
        return False
    
my_date_info = Date(2004, 10, 4) # create the object
second_date = Date(2004, 10, 4)
default_date = Date(2005)

# String representation
# print(my_date_info)

# Equality 
# print(my_date_info == second_date)
# print('Today\'s date is ', my_date_info)
# print(type(my_date_info))

old_day = Date(1998, 2, 10)
new_date = Date(2000, 2, 10)

print(old_day < new_date)

my_new_date = Date(2009, 6, 1)
print(my_new_date.is__leap__year())


'''
Exercise - Dog Class
'''






