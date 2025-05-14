from math import *
import random

a = sqrt(81)
print(a)

def main():
    # matrix = [[1,2,3],
    #           [4,5,6],
    #           [7,8,9]]
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

if __name__ == '__main__':
    main()