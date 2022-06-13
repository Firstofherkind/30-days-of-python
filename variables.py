# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:10:53 2022

@author: DELL
"""

# Hi, it's Day two. 
# Bult-in functions and variables.

#Built in functions are keywords available for use without having to import a library.
#The include len(), int()

first_name = 'Jennifer'
last_name = 'Egwu'
full_name = 'Egwu Jennifer Ifechukwudeni'
country = 'Nigeria'
city = 'Lagos'
age = 24
year = 2022
is_married = 'No'
is_true =  'True' 
is_light_on = 'No'
firstName, lastName, Age, sex = 'Jennifer', 'Egwu', 244, 'female'

#checking data types using the type() keyword.
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))

#using len()keyword

print(len(first_name))
print(len(first_name) > len(last_name))
print(len(last_name)  > len(last_name))
num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_two - num_one
print(diff)
product = num_one * num_two
print(product)
division = num_one/num_two
print(division)
exp = num_one ** num_two
print(exp)
remainder = num_two % num_one
print(remainder)
floor_division = num_one // num_two
print(floor_division)

#calculating raduis of a circle of 30 meters.
r = 30
pie = 22/7
area_of_circle = pie * (r ** 2)
print(area_of_circle)
print('4444444444444444444444444444444444444')
circum_of_circle = 2 * pie * r
print(circum_of_circle)

r = input('Enter the radius of the circle ')
a = area_of_circle
print(a)