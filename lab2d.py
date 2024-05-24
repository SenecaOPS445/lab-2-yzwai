#!/usr/bin/env python3
#
#name = 'Jon'
#age = 20
#print("Name: " + name)
#print("Age: " + str(age))
#print('Hi ' + name + ', you are ' + str(age) + ' years old.')

#name = input("Name: ")
#print("Name: " + name)
#age = input("Age: ")
#print("Age: " + age)

import sys

#arg = sys.argv[0]
#print(len(arg))
if len(sys.argv) != 3:
    print('Usage: ./lab2d.py name age')
    sys.exit()

name = sys.argv[1]
age = sys.argv[2]

print("Hi " + name + ', you are ' + age + ' years old.')



