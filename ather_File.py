def f1(x):
    return x+1

def f2(x):
    return x*2

def f3(x):
    return x**3

def my_map(func, my_lyst):
    new_m = []
    for i in my_lyst:
        mm = func(i)
        new_m.append(mm)
    return new_m

def main():
    m = [1,8,4,5]

    rez1 = list(map(f1,m))
    print(rez1)

    rez2 = my_map(f2, m)
    print(rez2)

    rez3 = my_map(f3, m)
    print(rez3)

if __name__ == '__main__':
    main()