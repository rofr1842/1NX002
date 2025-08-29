#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def myMinFunction(*args):
    if len(args) == 1:
        values = args[0]
    else:
        values = args

    if len(values) == 0:
        raise ValueError('myMinFunction() args is an empty sequence')

    smallest_value = args[0]
    for i, value in enumerate(values):
        if i == 0 or value < smallest_value:
            smallest_value = value

    return smallest_value

def printLower(*args, **kwargs):
    args = list(args)
    for i, value in enumerate(args):
        args[i] = str(value).lower()

    return print(*args, **kwargs)

def subtract(number1, number2):
    return number1 - number2

TOTAL = 0
def addToTotal(amount):
    global TOTAL
    TOTAL += amount
    return TOTAL

# Modify list with no return (by reference)
def remove_last_cat_from_list(petSpecies):
    if len(petSpecies) > 0 and petSpecies[-1] == 'cat':
        petSpecies.pop()

def callItTwice(func, *args, **kwargs):
    func(*args, **kwargs)
    func(*args, **kwargs)

# Lambda functions, also known as anonymous functions or nameless functions
def rectanglePerimeter(rect):
    return (rect[0] * 2) + (rect[1] * 2)

import random
def returnsTwoTypes():
    if random.randint(1, 2) == 1:
        return 42
    else:
        return 'forty two'

def isNumber(s):
    for char in s:
        if not char.isdigit():
            return False
    return True

def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, str) and x.isdigit():
        return True
    else:
        return False


if __name__ == "__main__":
    print(myMinFunction([0, 1,2,3,4,5,6,7,8,9]))
    print(myMinFunction(0, 1,2,3,4,5,6,7,8,9))
    #print(myMinFunction())

    name = 'Albert'
    printLower('Hello,', name)
    printLower('DOG', 'CAT', 'MOOSE', sep=': ')

    subtract(123, 987)

    print(addToTotal(10))
    print(addToTotal(10))
    print(addToTotal(9999))
    print(TOTAL)

    my_pets = ['dog', 'cat', 'bird', 'cat']
    print(my_pets)
    remove_last_cat_from_list(my_pets)
    print(my_pets)

    callItTwice(print, 'Hello, world!')

    myRectangle = [4, 10]
    print(rectanglePerimeter(myRectangle))
    # Lamda
    rectanglePerimeter = lambda rect: (rect[0] * 2) + (rect[1] * 2)
    print(rectanglePerimeter([4, 10]))

    rects = [[10, 2], [3, 6], [2, 4], [3, 9], [10, 7], [9, 9]]
    print(sorted(rects, key=lambda rect: (rect[0] * 2) + (rect[1] * 2)))

    mapObj = map(lambda n: str(n), [8, 16, 18, 19, 12, 1, 6, 7])
    print(list(mapObj))

    filterObj = filter(lambda n: n % 2 == 0, [8, 16, 18, 19, 12, 1, 6, 7])
    print(list(filterObj))

    print([str(n) for n in [8, 16, 18, 19, 12, 1, 6, 7]])
    print([n for n in [8, 16, 18, 19, 12, 1, 6, 7] if n % 2 == 0])

    hexNum1 = returnsTwoTypes()
    if isNumber(hexNum1):
        print(hex(hexNum1))
    else:
        print(type(hexNum1))

    hexNum2 = returnsTwoTypes()
    if isNumber(hexNum2):
        print(hex(hexNum2))
    else:
        print(type(hexNum2))



