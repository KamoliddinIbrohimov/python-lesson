"""
lessons on if and else

https://github.com/Kamoliddin777/python_lesson
"""
"""Homework"""
"""1.Create a list of new cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'], 
capitalize the first letter of the list item on the console. Make both letters 
uppercase for GM.
"""
   
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())
        
"""3.Perform the above exercise using an unequal (! =) Operator.
"""   
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())

"""4.Ask for a user login name. If the login is admin, "Welcome, Admin. Do you 
see a list of users?" message to the console. Otherwise, "Welcome, 
{user_name}!" output the text to the console.
"""    
admin = ['kamol','feruz','fayoz']
user_name = input('enter your name>>').lower()
for user in admin:
    if user == user_name:
        print('Welcome Admin')
        break
    else:
        print(f"Welcome {user_name.title()}")
        break
