# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 14:33:55 2022

@author: DELL
"""

#create an empty dict
dog = {}
student = {}


#check type
print(type(dog))

#add items
dog['Name'] = 'Bobby'
dog['Color'] = 'Brown'
dog['Breed'] = 'Labrador'
dog['legs'] = 'Short'
dog['Age'] = 2
print(dog)

student['firstName'] = 'Jennifer'
student['LastName'] = 'Egwu'
student['Gender'] = 'Female'
student['Age'] = 24
student['MaritalStatus'] = 'Single'
student['Skills'] = ['Python', 'Javascript']
student['City'] = 'Lagos'
student['Address'] = 'Satellite, Lagos'
 
print(student)
#Check the length of the dictionary

print('The length of the dictionary is:', len(student))


#Check what datatype the skill value is.
print('My skills are:', student['Skills'])
print(type(student['Skills']))

#Modifying the list
student['Skills'].append('GoLang')
student['Skills'].append('Kotlin')
print(student)
#dictionary keys as a list
print('The dictionary keys are:',student.keys())

#The dictionary values as a list
print('The dictionary values are:',student.values())

#Dictionary to a list of tuples
print(student.items())

#Delete one item in the dictionary
student.pop('firstName')
print(student)

#Permanently delete a dictionary.
del dog
