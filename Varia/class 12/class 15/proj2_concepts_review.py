from datetime import datetime

'''Write a program that will take the user's first name, and than the users last name, and print the value to a text file on 2 separate lines'''
# with open
# with open('fullname.txt','w') as output:
#     firstname = input('First name: ')
#     lastname = input('Last name: ')
#     output.write(f'{firstname}\n{lastname}')



# one method
# firstname = input('First name: ')
# lastname = input('Last name: ')

# f = open('my_output.tet', 'w') # we are opening a new file 
# f.write(f'{firstname}\n{lastname}')
# f.close()



''' Write a function called print_even_numbers that will take in a list of integer values and will extract the even numbers from that list and write to a text file let's try different parameters in our open function x, a, w'''



# This is our fuction
def find_even_number(my_list):
    output_list = []
    for m in my_list:
        if m % 2 == 0:
            output_list.append(m)

    # print(output)
    with open('even_nums.txt', 'w') as output:
        for o in output_list:
            o = str(o)
            output.writelines(o)



    print('File printed Successfully')

my_list = [1,2,3,4,5,6,7,12,14,15,21,22] # this is the date we pass into our function 


find_even_number(my_list) # this is our functione call 


''' Lets read in the song lyrics and put it into a list, but before we do, lets look at other options we have to read files in'''

with open('time_to_say_goodbye.txt','r') as lyrics:
     my_paragrah = lyrics.read() # will read in everything
     my_line = lyrics.readline()  # one line at a time 
     lyrics_list = lyrics.readlines() # will deliver a list 

# print(my_paragraph)
print(my_line)




''' Bank account class 
Create the bank account class per the specifications in the powerpoint.  
'''


# ac_no_1 = BankAccount("Toninho Takeo", 2345, "05-05-24", 1000 )
# ac_no_2 = BankAccount("Jim Jones", 5424, "01-05-22", 1000 )
# ac_no_3 = BankAccount("Sally Field", 3242, "11-04-15", 1000 )
# ac_no_4 = BankAccount("Burt Reynolds", 4325, "08-11-13", 1000 )





