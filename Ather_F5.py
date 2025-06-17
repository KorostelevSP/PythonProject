def main():
    colors = ['black', 'red', 'blue', 'green']
    # for ind, item in enumerate(colors):
    # for ind in range(colors):
    #     print(ind,colors[ind])

    for ind, item in enumerate(colors, 1):
        print(ind, item)

    # a = int(input())
    # while a % 2 != 0:
    #     a = int(input())
    # print(a)

    # i = 0
    # a = int(input())
    # while a != 0:
    #     a = a // 10
    #     i += 1
    # print(i)

    a = int(input())
    flag = 'No'
    while a != 0:
        if a % 10 == 7:
            flag = ('Yes')
            break
        a = a // 10
    print(flag)


if __name__ == '__main__':
    main()
