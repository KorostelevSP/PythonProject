from math import *
import random
import numpy as np

a = sqrt(81)
print(a)

a = [[1,2,3],
     [4,5,6],
     [7,8,9],
     [11,12,13]]

b = [[11,21,31],
     [41,51,61],
     [7,8,9],
     [12,12,12]]

def main_1test():

    # print(matrix[2][0])
    n = 3
    m = 4
    # 1 способ
    # matrix = []
    # for i in range(n):
    #     matrix.append([0]*m)

    # 2 способ
    # matrix = [0]*n
    # for i in range(n):
    #     matrix[i] = [0]*m

    # 3 способ
    matr_a = [[0] * m for i in range(n)]
    matr_b = [[0] * n for i in range(m)]
    for i in range(n):
        for j in range(m):
            random_number = random.randint(1, 10)
            matr_a[i][j] = random_number
            print(str(matr_a[i][j]).rjust(2), end=' ')
        print()

    print()

    for i in range(m):
        for j in range(n):
            random_number = random.randint(1, 10)
            matr_b[i][j] = random_number
            print(str(matr_b[i][j]).rjust(2), end=' ')
        print()

    m_a = len(matr_a[0])
    m_b = len(matr_b)
    if m_a == m_b:
        print('все норм')
    else:
        print('невозможно умножить')

    matr_c = [[0] * len(matr_a[0]) for i in range(len(matr_a))]
    for i in range(len(matr_a)):
        for j in range(len(matr_a[0])):
            matr_c[i][j] = matr_a[i][j] + matr_b[j][i]
    print(matr_c)

    for i in range(len(matr_a)):
        for j in range(len(matr_a[0])):
            print(str(matr_c[i][j]).rjust(2), end=' ')
        print()

def main():
    matrix1 = np.array(a)
    matrix2 = np.array(b)
    matrix3 = matrix1 + matrix2
    # matrix3 = np.add(matrix1,matrix2)
    # matrix3 = matrix1 - matrix2
    # matrix3 = np.subtract(matrix1, matrix2)
    # matrix3 = matrix1 * matrix2
    # matrix3 = np.dot(matrix1, matrix2)
    matrix3 = np.transpose(matrix3)
    print(matrix3)
    # matrix4 = np.zeros((3,3),dtype='int32')
    # matrix4 = np.ones((3, 3), dtype='int32')
    matrix4 = np.full((3, 3), 2,dtype='str')
    # matrix4 = np.amin(a)
    # matrix4 = np.amax(a)
    print(matrix4)

if __name__ == '__main__':
    main()