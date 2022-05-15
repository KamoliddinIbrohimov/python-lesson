"""
lessons on WORKING WITH LISTS

https://github.com/Kamoliddin777/python_lesson
"""
"""Homework"""

"""1.Make a list of countries you know and bring the list to the console
"""
states = ['USA', 'Irlandya', 'Dubay', 'Fransiya', 'USB']
print(states)

"""2.Extend the length of the list to the console
"""
print(len(states))

"""3.Use the sorted () function to sort the list on the console
"""
print(sorted(states))

"""4.Use sorted () to reverse the list on the console
"""
print(sorted(states, reverse=True))

"""5.Return the original list to the console
"""
print(states)

"""6.Use the reverse () method to start the list from the back
"""
states.reverse()
print(states)

"""7.Using the sort () method, drag the list to the console first in alphabetical 
order and then in reverse alphabetical order.
"""
states.sort()
print(states)

states.sort(reverse=True)
print(states)

"""8.Make a list of even numbers from 120 to 1200
"""
print(list(range(120, 1200,2)))

"""9.Calculate the sum of the numbers in the list and output it to the console
"""
print(sum(list(range(120, 1200,2))))

"""10.Calculate the difference between the largest and smallest number on the 
list and output it to the console
"""
nambers = list(range(120,1200,2))
print(max(nambers) - min(nambers))

"""11.Count the number of items in the list
"""
print(len(nambers))

"""12.Output 20 values ​​from the beginning, middle, and end of the list to the 
console
"""
print(nambers[:20])
print(nambers[-20:])
print(nambers[259:279])

"""13.create a list of dishes and include any 5 dishes you want
"""
dishes = ['osh', 'sumalak', 'non', 'kabop', 'somsa']

"""14.Copy the dishes to a new list called breakfast
"""
breakfast = dishes

"""15.In the new list, leave only the foods you eat for breakfast, and add 2 
more meals
"""
breakfast.remove('osh')
breakfast.remove('somsa')
breakfast.remove('kabop')

breakfast.append('tea')
breakfast.append('coofe')

print(breakfast)

"""16.Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
"""
print(dishes)
print(breakfast)

"""17.Turn the breakfast list above into a fixed list and try setting the 
breakfast to [0] = "cream and bread".
"""
breakfast= ('sumalak', 'non', 'tea', 'coofe')
breakfast[0] = "cream and bread"

print(breakfast)


































