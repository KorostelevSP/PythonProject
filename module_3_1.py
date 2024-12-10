#Счётчик вызовов
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(my_string=''):
    count_calls()
    my_tuple = (len(my_string), my_string.upper(), my_string.lower())
    return my_tuple

def is_contains(my_string='',list_to_search=[]):
    count_calls()
    my_string = my_string.lower()
    FunctionValue = False
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
        if my_string == list_to_search[i]:
            FunctionValue = True
    return FunctionValue

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)


