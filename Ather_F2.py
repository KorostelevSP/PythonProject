from functools import *

def my_reduce(func,my_list,init_list):
    rez = init_list
    for i in my_list:
        rez = func(rez,i)
    return rez

def f1(x,y):
    return x + y

def f2(x,y):
    return x * y

def main():
    m = [1,4,5,7]

    summ = 0
    rez1 = my_reduce(f1,m,summ)
    rez1_1 = reduce(f1,m,summ)
    print(rez1)
    print(rez1_1)

    mult = 1
    rez2 = my_reduce(f2, m, mult)
    rez2_2 = reduce(f2, m, mult)
    print(rez2)
    print(rez2_2)

if __name__ == '__main__':
    main()