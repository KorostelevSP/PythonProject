# def f1(x):
#     return x + 2

def main():
    # rez = f1(3)
    rez = lambda x: x + 2 if x==2 else 9
    rez2 = lambda x, y: x + y
    rez3 = lambda x, y, z: x + y + z
    rez4 = lambda *arg: sum(arg)
    rez5= lambda **arg: sum(arg.values())
    print(rez(3))
    print(rez2(3, 2))
    print(rez3(3, 2, 1))
    print(rez4(3, 2, 1, 6))
    print(rez5(one = 3, two = 2, thre = 1, four=6))

if __name__ == '__main__':
    main()
