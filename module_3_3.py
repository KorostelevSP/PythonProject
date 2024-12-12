# "Распаковка"

def print_params(a = 1, b = 'моя строка', c = True):
    print(a,b,c)

print_params()
print_params(3,"новая строка",False)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [7,'танк',True]
values_dict = {'a':5,'b':'из словаря','c':False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2,'строка из 2 списка']
print_params(*values_list_2, 42)