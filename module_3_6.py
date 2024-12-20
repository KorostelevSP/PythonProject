# "Подробнее о функциях."
def calculate_structure_sum(structure):
    my_sum = 0
    my_local_rez = 0
    for i in structure:
        if isinstance(i,list) or isinstance(i,tuple) or isinstance(i,set):
            my_local_rez = calculate_structure_sum(i)
            my_sum += my_local_rez
        elif isinstance(i,dict):
            for key,value in i.items():
                my_sum += len(key)
                if isinstance(value, list) or isinstance(value, tuple) or isinstance(value, set):
                    my_local_rez = calculate_structure_sum(value)
                    my_sum += my_local_rez
                elif isinstance(value, int) or isinstance(value, float):
                    my_sum += value
                elif isinstance(value, str):
                    my_sum += len(value)
        elif isinstance(i,int) or isinstance(i,float):
            my_sum += i
        elif isinstance(i, str):
            my_sum += len(i)
        else:
            print(type(i))
    return my_sum

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

global_rezult = calculate_structure_sum(data_structure)
print(global_rezult)