#!/usr/bin/env python3
#
#name = 'Jon'
#age = 20
#print("Name: " + name)
#print("Age: " + str(age))
#print('Hi ' + name + ', you are ' + str(age) + ' years old.')

import sys

#name = input("Name: ")
#print("Name: " + name)
#age = input("Age: ")
#print("Age: " + age)

name = sys.argv[1]
age = sys.argv[2]

print("Hi " + name + ', you are ' + age + ' years old.')
