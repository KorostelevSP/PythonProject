# Задание:

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Переменные: количество участников первой команды (team1_num).
print('В команде %(name)s, участников: %(team1_num)d ! ' % {'name':'Мастера','team1_num':team1_num})

# Переменные: количество участников в обеих командах (team1_num, team2_num).
print('Итого сегодня в командах участников: %(team1_num)d и %(team2_num)d !' % {'team1_num':team1_num,'team2_num':team2_num})

# Переменные: количество задач решённых командой 2 (score_2).
print('Команда Волшебники данных решила задач: {score_2} !'.format(score_2 = score_2))

# Переменные: время за которое команда 2 решила задачи (team1_time).
print('Волшебники данных решили задачи за {team1_time} с !'.format(team1_time = team1_time))

# Переменные: количество решённых задач по командам: score_1, score_2
print(f'Команды решили {score_1} и {score_2} задач.')

# Переменные: исход соревнования (challenge_result).
print(f'Результат битвы: победа команды Мастера кода!')

# Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'