# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 20:49:00 2022

@author: DELL
"""
#declare an empty list
empty = []
empty = list()

#list with 5 items
fruits = ['apple','mango', 'grape', 'orange', 'pineapple']

#length of list
print(len(fruits))

#first, middle and last item on the list

print(fruits[0])
print(fruits[2])
print(fruits[-1])

mixed_data_type = ['Jennifer', 24, 155, 'single', 'Nigeria']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(mixed_data_type)
print(it_companies)
#number of companies
print(len(it_companies))

#first, last and middle
print('first:', it_companies[0])
print('middle:', it_companies[2:3])
print('last:', it_companies[4:])

#modifying a lisst

print(it_companies.insert(2, 'Datacamp'))
print(it_companies[2].upper())

#Joining lists
print(it_companies + fruits)

#value in list
print('Datacamp' in it_companies)
print('DATACAMP' in it_companies)

#sorting lists
print(it_companies.sort())

#slicing

print(it_companies[0: 4])
print(it_companies[-4:-1])

#deleting a list and clearing a list
del it_companies[0]
print(it_companies)
it_companies.clear()
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React']
back_end = ['Python', 'Express', 'Node']

join = front_end + back_end
full_stack = join.copy()
print('Old:', full_stack)

#numbers
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
sort = ages.sort()
print(sort)