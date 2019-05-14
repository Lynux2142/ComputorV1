#!/usr/bin/python3

import sys
from math import *

def getDatasDegree(av):
    datas = av.split()
    degree = 0
    for elem in datas:
        if (elem[0] == 'X'):
            degree = int(elem[2]) if (int(elem[2]) > degree) else degree
    return datas, degree

def reduceEqu(datas, degree):
    values = [0.0 for i in range(0, degree + 1)]
    sign = 1.0
    for i in range(0, len(datas)):
        if (datas[i] == '='):
            sign = -1.0
        if (datas[i][0] == 'X'):
            type(datas[i - 2])
            values[int(datas[i][2])] += float(datas[i - 2]) * (-1.0 if (datas[i - 3] == '-') else 1.0) * sign
    return values

def printEqu(values, degree):
    sys.stdout.write('reduced form: ')
    for i in range(0, degree + 1):
        sys.stdout.write('{} {} * X^{} '.format('-' if (values[degree - i] < 0) else '+', abs(values[degree - i]), degree - i))
    print('= 0')

def main():
    if (len(sys.argv) != 2):
        print('usage: ./ComputorV1 [equation]')
        return (0)
    datas, degree = getDatasDegree(sys.argv[1])
    values = reduceEqu(datas, degree)
    printEqu(values, degree)
    print('Ploynomial degree: {}'.format(degree))
    if (degree > 2):
        print("The polynomial degree is stricly greater than 2, I can't solve.")
        return (0)
    if (degree == 0):
        if (values[0] != 0):
            print('Infinity of Solutions')
        else:
            print('No Solution')
    elif (degree == 1):
        print('One Solution:')
        print('x = {}'.format(-values[0] / values[1]))
    elif (degree == 2):
        print('Two Solutions:')
        delta = pow(values[1], 2) - 4.0 * values[2] * values[0]
        if (delta > 0):
            print('x1 = {}'.format((-values[1] - sqrt(delta)) / (2.0 * values[2])))
            print('x2 = {}'.format((-values[1] + sqrt(delta)) / (2.0 * values[2])))
        elif (delta == 0):
            print('x = {}'.format(-values[1] / (2.0 * values[2])))
        else:
            print('No Solution')
    return (1)

if __name__ == '__main__':
    main()
