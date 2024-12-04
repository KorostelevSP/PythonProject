grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_list = list(students)
my_list.sort()
# sorted(my_list)
print(my_list)
end = len(my_list)
for i in range(0, end):
    numbers = grades[i]
    totalsum = sum(numbers)
    totalLen = len(numbers)
    myArithmeticMean = totalsum / totalLen
    NameStudent = my_list[i]
    print('Имя студента :', NameStudent, ' средняя оценка: ', myArithmeticMean)
