'''
Print all names with last name 'Smith'.
'''

def name(first_name, last_name):
    lastname = last_name.lower()
    if lastname == 'smith':
        return("Name: " + first_name + ", " + last_name)
    else:
        return ("Last name is not Smith!")



print(name("Andrew", "Smith"))
print(name("Sally", "Smith"))
print(name("Lily", "Lee"))
print(name("Sam", "Smith"))
print(name("David", "Kim"))


