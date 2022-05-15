"""
lessons on the list

https://github.com/Kamoliddin777/python_lesson
"""
#Homevork

"""1.create a list of names and enter the names of at least 3 close friends
"""
names = ['suxrob', 'olim', 'bexruz']

"""2.Write a short message to each friend on the list and send it to the console:
"""
print(f'Salom {names[0].title()} bugun {names[1].title()} {names[2].title()} bilan choyhonaga boramizmi?')

"""3.create a list called numbers and upload different numbers into it (positive, negative, whole, decimal).
"""
nambers = [564, -879, 5.64, 0.965]

"""4.Try different arithmetic operations on the numbers in the list above. Change the value of some of 
the numbers in the list, and replace some.
"""
print(nambers[0]+nambers[1]-nambers[3]*nambers[2]/nambers[3])
nambers[0] = 56
nambers[2] = 7.65

"""5.Make two lists, t_persons and z_persons, and enter the names of the historical figures you respect the most, 
and the names of the living people of our time.
"""

t_persons = ['Alisher Navoiy', 'Beruniy', 'Farobiy']
z_persons = ['Yulduz Usmonova', 'Jahongir foziljonov', 'Botir Qodirov']

"""6.Extract one value from each of the above lists (.pop ()) and display it as follows:
"""
print(f'I would like to talk to {z_persons.pop(0)},{t_persons.pop(0)} a historical figure')

"""7.Create a blank list named friends and add your friends you want to invite to 5-6 guests using .append ().
"""

friends = []

friends.append('Jamshid')
friends.append('Baxtiyor')
friends.append('Feruz')
friends.append('Farhod')
friends.append('Iskandar')
friends.append('Olim')
print(friends)

"""8.Delete people from the list above who are unable to visit using the .remove () method.
"""
friends.remove('Feruz')
friends.remove('Jamshid')
print(friends)

"""9.Add new names to the end, beginning, and middle of the list.
"""

friends.insert(0, 'Feruz')
friends.insert(-1, 'Jamshid')
friends.insert(4, 'Ruslan')
print(friends)

"""9.Create a blank list called New Guests. Using the .pop () and .append () methods, 
extract the name of your visiting friend from the friends list and add it to the guest list.
"""
guests = []

guest0 = friends.pop(0)
guest1 = friends.pop(2)
guest2 = friends.pop(4)
guests.append(guest0)
guests.append(guest1)
guests.append(guest2)

print(guests)





















