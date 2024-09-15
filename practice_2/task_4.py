# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""


def readInt(hint):
    try:
        print(hint)
        val = int(input())
        print()
        return val
    except ValueError:
        return None


number = readInt("Enter your number:")

if number is None:
    print("Failed to read number")
    exit()

if number < 1000 or number > 9999:
    print("Number should contain only 4 digits")
    exit()

x = number
y = 0

digits = []

while x > 0:
    digit = x % 10
    y += digit
    x //= 10
    digits.append(str(digit))

digits.reverse()

print(f'{' + '.join(digits)} = {y}')
