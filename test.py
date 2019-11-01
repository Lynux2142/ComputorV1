#!/usr/local/bin/python3

import sys
import re

def reduce_equation(equation):
    equation = sys.argv[1].strip()
    equation = equation.replace(' ', '')
    equation = equation.lower()
    return (equation)

def split_equal(equation):
    return (equation.split('='))

def split_elem(equation, chars):
    array = []
    i = 0
    for j in range(0, len(equation)):
        if (chars.find(equation[j]) != -1):
            array.append(equation[i:j])
            i = j
    array.append(equation[i:])
    return (array)

def split_into_array(equation):
    array = []
    array.append(split_elem(equation[0], '+-'))
    array.append(split_elem(equation[1], '+-'))
    return (array)

def mul(a, b):
    return ((0.0 if (a == '') else float(a)) * (0.0 if (b == '') else float(b)))

def div(a, b):
    return ((0.0 if (a == '') else float(a)) / (0.0 if (b == '') else float(b)))

def make_calc(calc):
    calc_functs = [mul, div]
    calc_chars = ['*', '/']
    array = re.split('([/\*])', calc)
    res = 0

    print(array)

def reduce_elem(equation):
    a = 0
    b = 0
    c = 0
    for elem in equation[0]:
        if (elem.find('x^2') != -1):
            value = make_calc(elem.replace('x^2', ''))
            print(value)

def main():
    if (len(sys.argv) != 2):
        print("usage: ./computorV1 [equation]")
        sys.exit(1)
    equation = reduce_equation(sys.argv[1])
    print(equation)
    equation = split_equal(equation)
    print(equation)
    equation = split_into_array(equation)
    print(equation)
    reduce_elem(equation)

if __name__ == '__main__':
    main()
