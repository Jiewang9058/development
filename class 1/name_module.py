
full_name = "full_first_name"+ "full_last_name"
def full_name(full_first_name,full_last_name):
     return f"{full_first_name} {full_last_name}"


def reverse_name(first_name,last_name):
     return f"{last_name} {first_name}"


def get_iniatials(first_name,last_name):
     first_name = input("please enter first name:")
     last_name = input("Please enter last name:")
     return f'{first_name[0]}.{last_name[0]}'

