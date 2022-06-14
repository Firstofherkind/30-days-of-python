# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 17:12:28 2022

@author: DELL
"""

age = 24
height = 155.0
com_num = 2 + 1j


height = input('Please enter your height: ')
base = print('Please enter the base: ')
print('The area of the triangle is: ', base * height)

a = input('Please enter side a: ')
b = input('please enter side b: ')
c = input('Please enter side c: ')
print('The perimeter of the triangle is: ', a+b+c)

length = input('please enter the length: ')
width = input('Please enter the width: ')
print('The perimeter of the square is: ', 2 *(length + width))

Radius =  input('Please enter radius: ')
pi = 3.14
print('The area of the circle: ', pi * (Radius ** 2))
print('The circumference of the circle is: ', 2 * pi* Radius)

print(len('python') < len('dragon'))
print('on' in 'Python' and 'on' in 'dragon')

print('jargon','jargon' in 'I hope this course is not full of jargon')
print('jargon','on' not in 'python' and 'on' not in 'dragon')

print(int(len('python')), float(len('python')))