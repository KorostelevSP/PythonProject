# "Стиль кода часть II. Цикл While"

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
len_my_list = len(my_list)
i = 0
while i < len_my_list:
    if my_list[i] == 0:
        i = i + 1
        continue
    elif my_list[i] < 0:
        break
    print(my_list[i])
    i = i + 1
