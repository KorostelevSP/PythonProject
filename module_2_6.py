# "Слишком древний шифр"

StartingCharacter = 1
EndCharacter = 21

while True:
    my_password = ""
    NumberFirstCell = int(input('Введите число от 3 до 20: '))
    if NumberFirstCell >= 3 and NumberFirstCell <= 20:
        for i in range(StartingCharacter, EndCharacter):
            for j in range(StartingCharacter, EndCharacter):
                NumberСhecks = i + j
                if i < j and NumberFirstCell %NumberСhecks == 0:
                    my_password = my_password + str(i) + str(j)

        print('Ваш пароль :', my_password)
        break
    else:
        print('Введите правильное число!')
        continue
