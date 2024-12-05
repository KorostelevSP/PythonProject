# "Условная конструкция. Операторы if, elif, else"

first  = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third  = int(input('Введите третье число: '))

NumberMatches =  0
if first==second and  second==third:
    NumberMatches = 3
elif first==second or first==third or second==third:
    NumberMatches = 2
else:
    NumberMatches = 0

print('Количество совпадений: ',NumberMatches)