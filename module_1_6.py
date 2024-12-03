# module_1_6
my_dict = {'Сергей': 1987, 'Александр': 1980, 'Петя': 1995}
print(my_dict)

my_dict.update({'Никита': 1998, 'Елена': 1999})
print(my_dict)

birthday = my_dict.pop('Сергей')
print(birthday)
print(my_dict)

my_set = {1, 1, 22, 33, 22, (1, 12, 2), 'Вася'}
print(my_set)
my_set.update({13, 'Sergei'})
my_set.add(78)
print(my_set)

my_set.remove('Вася')
print(my_set)
