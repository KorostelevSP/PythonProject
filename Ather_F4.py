def main():
    def f():
        for i in m:
            if not i:
                return False
        return True

    def f1():
        for i in m:
            if i:
                return True
        return False

    n = {1: 'one', 2: 'two', 3: 'thee'}
    m = [6, 12, 9, 21]
    # rez = f()
    # rez = all(n)
    rez = all(map(lambda x: x % 3 == 0, m))
    print(rez)

    for i in range(10, 25, 3):
        if i % 2 == 0:
            print(i, end=" ")
    print()

    i =0
    while i<10:
        print(i, end=" ")
        i+=1
    print()
    
    n = [1,2,30,4,5]
    # rez1 = f1()
    # rez1= any(map(lambda x: True if x>=5 else False,n))
    rez1 = any(map(lambda x:  x % 5==0, n))
    print(rez1)

if __name__ == '__main__':
    main()
