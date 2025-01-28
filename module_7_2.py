# Задача "Записать и запомнить":

def custom_write(file_name, strings):
    file = open(file_name, 'w',encoding='utf-8')
    my_dct = {}
    print(my_dct)
    for i in range(len(strings)):
        my_tupl = (i+1,file.tell())
        file.write(f'{strings[i]}\n')
        my_dct.setdefault(my_tupl, strings[i])
        # my_dct.setdefault(my_tupl, []).append(strings[i])
    file.close()
    return my_dct
    # print(my_dct)

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)