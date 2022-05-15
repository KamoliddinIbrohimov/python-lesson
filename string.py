"""
lessons on the string

https://github.com/Kamoliddin777/python_lesson
"""
#Homework
"""1.Do the following exercises:
street = "Gardener"
mahalla = "Sogbon"
district = "Bodomzor"
region = "Samarkand"
"""
street = "Gardener"
mahalla = "Sogbon"
district = "bodomzor"
region = "Samarqand"

"""2.Summarize the above variables and output them to the console in the following view:
Bogbon street, Sogbon mahalla, Bodomzor district, Samarkand region 
"""
print(f'{street} street, {mahalla} mahalla, {district} district, {region} region')

"""3.Ask the user for the value of the above variables (street, mahalla, district, province). 
And repeat the previous exercise."""

print("please enter details!")
street = input("street:")
mahalla = input("mahalla:")
district = input("district:")
region = input("region:")
print(f'{street} street, {mahalla} mahalla, {district} district, {region} region')

"""4.When outputting the above text to the console, type a new line after each comma
"""
print(f'{street} street,\n{mahalla} mahalla,\n{district} district,\n{region} region.')

"""5.Using the f-string, load the above text into a new, addressable variable
"""
manzil = f'{street} street, {mahalla} mahalla, {district} district, {region} region'

"""6.Use the title (), upper (), lower (), and capitalize () methods we learned above.
"""
print(f'{street.title()} street, {mahalla.lower()} mahalla, {district.capitalize()} district,{region.upper()} region')
































