#Дополнительное практическое задание по модулю: "Базовые структуры данных."
#module_1_7

#Исходные данные:
#Списки оценок учеников, в алфавином порядке
grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,4,5]]
#Список студентов
students={'Johnny','Bilbo','Steve','Khendrik','Aaron'}

#Вытаскиваем имена студентов и присваиваем их переменным
name1=students.pop()
name2=students.pop()
name3=students.pop()
name4=students.pop()
name5=students.pop()

#Создаем список из имен студентов
students_new=[name1, name2, name3, name4, name5]

#Сортируем новый список студентов по алфавиту
students_new.sort()
print("Cписок студентов по алфавиту :")
print(students_new)

#Вытаскиваем оценки и присваиваем их переменным
grades5=grades.pop()
grades4=grades.pop()
grades3=grades.pop()
grades2=grades.pop()
grades1=grades.pop()

#Вычисляем среднюю оценку
middle_grades1=(sum(grades1)/len(grades1))
middle_grades2=(sum(grades2)/len(grades2))
middle_grades3=(sum(grades3)/len(grades3))
middle_grades4=(sum(grades4)/len(grades4))
middle_grades5=(sum(grades5)/len(grades5))

#Из средних оценок составляем список
list_middle_grades=[middle_grades1,middle_grades2,middle_grades3,middle_grades4,middle_grades5]
print("Список средних оценок: ")
print(list_middle_grades)

#Составляем словарь из списка фамилий students_new и списка средних оценок list_middle_grades
# пары: students_new[*] - list_middle_grades[*]

dict={students_new[0]:list_middle_grades[0],students_new[1]:list_middle_grades[1],students_new[2]:list_middle_grades[2],students_new[3]:list_middle_grades[3],students_new[4]:list_middle_grades[4]}
print("Итог - словарь будет иметь вид: ")
print(dict)