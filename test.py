#!/usr/local/bin/python3

import sys
import re
from math import sqrt

def split_and_clear(equation):
    return (sys.argv[1].strip().replace(' ', '').lower().split('='))

def split_elem(equation, chars):
    array = []
    i = 0
    for j in range(0, len(equation)):
        if (chars.find(equation[j]) != -1 and j != 0):
            array.append(equation[i:j])
            i = j
    array.append(equation[i:])
    return (array)

def split_into_array(equation):
    array = []
    for elem in equation:
        array.append(split_elem(elem, '+-'))
    return (array)

def mul(a, b):
    return ((0.0 if (a == '') else float(a)) * (0.0 if (b == '') else float(b)))

def div(a, b):
    return ((0.0 if (a == '') else float(a)) / (0.0 if (b == '') else float(b)))

def make_calc(calc):
    calc_functs = [mul, div]
    calc_chars = ['*', '/']
    array = re.split('([/\*])', calc)
    for i in range(0, len(array)):
        if (array[i] == '-'):
            array[i] = -1.0
        elif (array[i] == '' or array[i] == '+'):
            array[i] = 1.0
    res = 0.0
    i = 0
    while (len(array) != 1):
        for char, funct in zip(calc_chars, calc_functs):
            if (array[i] == char):
                res = funct(array[i - 1], array[i + 1])
                del array[i - 1:i + 2]
                array.insert(0, res)
                i = 0
        i += 1
    res = float(array[0])
    return (res)

def reduce_elem(equation):
    a = 0
    b = 0
    c = 0
    for i in range(0, len(equation)):
        sign = 1.0 if (i == 0) else -1.0
        for elem in equation[i]:
            if (elem.find('x^2') != -1):
                a += sign * make_calc(elem.replace('x^2', ''))
            elif (elem.find('x') != -1):
                b += sign * make_calc(elem.replace('x', ''))
            else:
                c += sign * make_calc(elem)
    return (a, b, c)

def main():
    if (len(sys.argv) != 2):
        print("usage: ./computorV1 [equation]")
        sys.exit(1)
    equation = split_and_clear(sys.argv[1])
    print(equation)
    equation = split_into_array(equation)
    print(equation)
    a, b, c = reduce_elem(equation)
    print('{}x^2 + {}x + {} = 0'.format(a, b, c))
    delta = b ** 2 - 4 * a * c
    print('delta = {}'.format(delta))
    if (delta > 0):
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        print('x1 = {}\nx2 = {}'.format(x1, x2))
    elif (delta == 0):
        x = -b / (2 * a)
        print('x = {}'.format(x))
    else:
        print('pas de solution reel')

if __name__ == '__main__':
    main()
