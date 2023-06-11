# -*- coding: utf-8 -*-

# A simple calculator

def add(*numbers):
    return sum(numbers)

def deduct(number1 : int, number2 : int):
    return number1 - number2

def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def divide(number1 : int, number2 : int):
    return number1 / number2

