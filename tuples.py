# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 03:28:18 2022

@author: DELL
"""
#creating an empty tuple
tuple = ()

brothers = ('Anthony','Daniel')
sisters = ('Vanessa', 'Chidera')
siblings = brothers + sisters
print(siblings)
#print(siblings.count())

mum_dad = ('Ngozi', 'ANthony')

fam = siblings + mum_dad
print(fam)

*siblings, mum, dad = fam
print(siblings)
print(mum)
print(dad)

friuts = ('Mango', 'Apple', 'Orange')
vegetables = ('lettuce', 'Pumkin', 'Brocolli')
animal = ('Meat', 'milk')

food = friuts + vegetables + animal
print(food)
food_lst = list(food)
print(food_lst)

