# user input for their desire module code
module = input("Enter a module code: ")

# this is a dictionary function in python to lookup for module code and module name
switch = {
    'CSC1006':'Mathematics 2',
    'CSC1007':'Operating System',
    'CSC1008':'Data Structures and Algorithms',
    'CSC1009':'Object-Oriented Programming',
    'CSC1010':'Compurer Networks'
}

# print result
print(switch[module])