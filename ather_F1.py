
def f1(x):
    return x > 0

def f2(x):
    return x > 5

def f3(x):
    return x % 2

def my_filter(func,my_list):
    new_m = []
    for i in my_list:
        if func(i):
            new_m.append(i)
    return new_m

def main():
    m=[3,4,-6,7]
    new_m = []
    for i in m:
        if f1(i):
            new_m.append(i)
    print(new_m)
    rez1 = list(filter(f1,m))
    print(rez1)

    new_n = my_filter(f2,m)
    print(new_n)
    rez2 = list(filter(f2, m))
    print(rez2)

    new_k = my_filter(f3,m)
    print(new_k)

if __name__ == '__main__':
    main()