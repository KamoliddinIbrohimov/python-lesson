"""
lessons on the check the conditions

https://github.com/KamoliddinIbrohimov/python-lesson"""
"""Homework"""

"""1.Ask the user to enter an even number. If the user enters an even number, 
"Thank you!", If the user enters an odd number, display the message "This 
number is not even"
"""
number = int(input("Enter an even number\n>>"))
if number%2==0:
    print("Thank you:)")
else:
    print("Enter an even number:(")
    
"""1.Ask for the age of the user, and calculate the ticket price for admission 
to the museum as follows:
"""
age = int(input("Enter your age\n>>"))
if age<4 or age>60:
    price = "free"
elif age<18:
    price = "10000 so'm"
else:
    price = "20000 so'm"
print(f"ticket price for you {price}")

"""3.Ask the user to enter two numbers, compare the numbers, and display a 
message about whether they are equal or large / small.
"""
number1 = int(input("enter the first number>>"))
number2 = int(input("enter the second  number"))
if number1==number2:
    result = "equal"
    print(f"{number1}{result}{number2}")
elif number1>number2:
    result = f"{number1} big {number2}"
else:
    result = f"{number1} small {number2}"
print(result)    

"""4.create a list of products and include at least 10 different products. 
Create a new, empty list called Basket and ask the user to add at least 5 
items to the cart. Compare the items in the cart with the list of products, 
and display which one is on the list, "Product is in our store," otherwise, 
"Product is not in our store."
"""
    
products = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

basket = []

for n in range(5):
    basket.append(input(f"enter the {n+1} product"))
    

for product in basket:
    if product in products:
        print(f"{product} we have")
    else:
        print(f"{product} we do not have")
 
"""5.create a list of users, and add at least 5 logins. Ask the user to select 
a new login and compare the login entered by the user with the contents of the 
list of users. If there is such a login in the list, "Login busy, choose a new 
login!" otherwise "Welcome, user!" output the message
"""

products = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

basket = []
have = []
no = []
for n in range(5):
    basket.append(input(f"enter the {n+1} product"))
    
for product in basket:
    if product in products:
        have.append(f"{product} have")
    else:
        no.append((f"{product} no"))
        
if len(no)==0:
    print("we have all the products you choose")
else:
    print(f"we have no {no}")
    
"""6.create a list of users, and add at least 5 logins. Ask the user to select
a new login and compare the login entered by the user with the contents of the
list of users. If there is such a login in the list, "Login busy, choose a new 
login!" otherwise "Welcome, user!" output the message.
"""
users = ['alisher','aziza','yasina','umar']

for user in users :
    login = input("Enter a new login>>")
    if login in user:
        print(f"{login}: it has a login")
    else:
        print(f"{login}: accepted")
        users.append(login)
        break
        
"""7.Ask the user to enter an integer. Display the number entered by the user 
on the console to which of the numbers from 2 to 10 is divisible by the 
remainder.
""" 
number3 = int(input("enter the whole number"))

for n in range(2,11):
    if number3%n==0:
        print(f"{number3} {n} is divided by the remainder")
    else:
        print()
    
        
    




































