#!/usr/local/bin/python3

import sys
import re
import sys
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

def reduce_elem(elem):
    array = list(filter(None, re.split(r'([\*\/]?)([+-]?[\d]+\.?[\d]*)\*?(x\^)([+-]?[\d]+)', elem)))
    value = float(array[0])
    expo = int(array[2])
    for i in range(3, len(array), 4):
        if (array[i] == '*'):
            value *= float(array[i + 1])
            expo += int(array[i + 3])
        elif (array[i] == '/'):
            value /= float(array[i + 1])
            expo -= int(array[i + 3])
    return ((value, expo))

def group_X(equation):
    array = []
    for side in equation:
        tmp = []
        for elem in side:
            tmp.append(reduce_elem(elem))
        array.append(tmp)
    return (array)

def reduce_equ(equation):
    array = []
    tmp = {}
    for i in range(len(equation)):
        sign = 1.0 if (i == 0) else -1.0
        for elem in equation[i]:
            if elem[1] in tmp:
                tmp[elem[1]] += (sign * elem[0])
            else:
                tmp[elem[1]] = (sign * elem[0])
    for i in sorted(tmp.keys(), reverse = True):
        array.append((tmp[i], i))
    return (array)

def print_infos(equation):
    sys.stdout.write('Reduced form:')
    for elem in equation:
        sys.stdout.write(f" {'+' if (elem[0] >= 0) else '-'} ")
        if (elem[1] > 1):
            sys.stdout.write(f'{abs(elem[0])}x^{elem[1]}')
        elif (elem[1] == 1):
            sys.stdout.write(f'{abs(elem[0])}x')
        else:
            sys.stdout.write(f'{abs(elem[0])}')
    print(' = 0.0')
    print(f'Polynomial degree: {equation[0][1]}')

def pgcd(value1, value2):
    if (value2 == 0):
        return value1
    else:
        r = value1 % value2
        return (pgcd(value2, r))

def solve_2nd(equation):
    delta = equation[1][0] ** 2 - 4 * equation[0][0] * equation[2][0]
    if (delta > 0):
        print('Discriminant is strictly possitive, the two solutions are:')
        print(f'{(-equation[1][0] - sqrt(delta)) / (2 * equation[0][0])}')
        print(f'{(-equation[1][0] + sqrt(delta)) / (2 * equation[0][0])}')
    elif (delta == 0):
        print('Discriminant is equal to zero, the solution is:')
        print(f'{-equation[1][0] / (2 * equation[0][0])}')
    else:
        print('Discriminant is strictly negative, the two solutions are:')
        lower_div = 2 * equation[0][0]
        print(f'{-equation[1][0] / lower_div} - {sqrt(-delta) / lower_div}i')
        print(f'{-equation[1][0] / lower_div} + {sqrt(-delta) / lower_div}i')

def solve_1rst(equation):
    print('The solution is:')
    print(f'{-equation[1][0] / equation[0][0]}')

def solve_nothing(equation):
    if (equation[0][0] == 0):
        print('All real numbers are solution of the equation')
    else:
        print('The equation is insoluble')

def solve_equation(equation):
    if (equation[0][1] == 2):
        solve_2nd(equation)
    elif (equation[0][1] == 1):
        solve_1rst(equation)
    else:
        solve_nothing(equation)

def main():
    if (len(sys.argv) != 2):
        print("usage: ./computorV1 [equation]")
        sys.exit(1)
    equation = split_and_clear(sys.argv[1])
    equation = split_into_array(equation)
    equation = group_X(equation)
    equation = reduce_equ(equation)
    print_infos(equation)
    if (0 <= equation[0][1] <= 2):
        solve_equation(equation)
    else:
        print("The polynomial degree is stricly greater than 2, I can't solve.")

if __name__ == '__main__':
    main()
