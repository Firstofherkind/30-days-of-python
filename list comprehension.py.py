# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 23:27:31 2022

@author: DELL
"""

#list comprehension

#filter o and negative number from the list using list comprehension
nums = [-4, -3, -2, -1, 0, 2, 4, 6]
filter =[(num) for num in nums if num <= 0]
print(filter)


#flatten a list of list of list.
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten = [num for row in list_of_lists for num in row]
final = [num for row in flatten for num in row]
print(final)

#Create a list of list of tuples into a list of dictionary.
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat = [num for row in countries for num in row]
new = [{'Country' : a, 'City': b} for a, b in flat]
print(new)


#create a list of list of tuples into a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_names = [word for row in names for word in row]
print(new_names)
new = [(a + ' ' + b) for a,b in new_names]
print('Concatinated string of tuples:', new)

#Print list of list with items in lists as caps and with caps initials in the middle
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_con = [country for row in countries for country in row]
list_con = [[a.upper(), a[:3].upper(), b.upper()] for a, b in new_con ]
print(list_con)
 
#print squares of a number to form a tuple of numbers.
list_num = [(num, 1, num*1, num **2, num ** 3, num ** 4, num ** 5) for num in range(11)]
print(list_num)