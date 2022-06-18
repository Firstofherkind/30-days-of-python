# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 13:58:53 2022

@author: DELL
"""

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#lenth of a set

print('The length of it_companies is:', len(it_companies))

#adding to a set
com = {'twitter'}
print(it_companies.union(com))
print(A.union(B))
print(A.intersection(B))
print('Join B with A:',  B.union(A))
print('Join A with B:', A.union(B))


#remove an item from a list
it_companies.remove('Apple')
print(it_companies)
#or use pop
it_companies.pop()
print(it_companies)
#The remove keyword removes a specified word while the pop()function removes any specified wordi a set

#subset of sets. Thisis used to check if a set is a smaller part of a set.
print(A.issubset(B))
#Disjoints are also used to check if a set is a part of a set
print(A.isdisjoint(B))
print(B.isdisjoint(A))
#To completely delete sets we use the del keyword.
del A
del B

#converting fron list to set
#NB: List can have duplicates while sets does not have duplicates.
new_age = set(age)
print(new_age)
print(len(new_age))
print(len(age))
