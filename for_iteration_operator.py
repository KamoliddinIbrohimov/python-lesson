"""
lessons on for iteration operator

https://github.com/Kamoliddin777/python_lesson
"""
"""Homework"""

"""1.Make a list of names of at least 5 items, and write a repeating message 
for each name on the list
"""
names = ['Farxot', 'Iskandar', 'Feruz', 'Fayoz','Shoxrux']
x = 0
for n in names:
    print(f'Hellov {n}')
    x +=1
"""2.When the above cycle is complete, display the message "Code repeated n 
times" (write how many times the code was repeated instead of n)
"""
print(f'code was repeated {x} times')

"""4.Make a list of odd numbers from 10 to 100. Move the cube of each item in 
the list from the new row to the console.
"""
for n in list(range(9,100,2)):
    print(n**3)
    
"""5.Ask the user to add 5 favorite movies, and save it to the list of movies. 
Display the result on the console.
"""
movies = []
for m in range(5):
    movies.append(input(f'{m + 1} - movies:'))
print(movies)

"""6.Ask the user how many people they have met (talked to) today, and write 
the name of each person they interviewed individually. Upload the list to the 
console.
"""
names = []
namber = int(input('How many people did you talk to today>>'))

for n in range(namber):
    names.append(input(f'The {n + 1} person you talk to>>').title())
print(names)





























































