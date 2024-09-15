# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""

def readFloat(hint):
    try:
        print(hint)
        val = float(input())
        print()
        return val
    except ValueError:
        return None

weight = readFloat("Enter your weight in kg:")
height = readFloat("Enter your height in m:")

if weight is not None and height is not None:
    bmi = weight/height**2
    print(f'Your BMI is {bmi:.2f} kg/m^2')
else:
    print('Failed to compute BMI, please check your input.')
