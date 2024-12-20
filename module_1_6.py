#Практическое задание по теме: "Словари и множества"

#Создаем переменную my_dict и делаем ее словарем из пар "имя"-"год рождения"
my_dict={'Name1':1962, 'Name2':2000, 'Name3':2100,'Name4':3000}
#Выводим словарь на экран
print("Наш словарь my_dict: ",end='')
print(my_dict)

#Выводим на экран одно значение по существующем ключу, одно по отсутствующему ключу
print("Элемент словаря  существующий:")
print("my_dict [Name1] =", end='')
print(my_dict['Name1'])

#Отсутствующий в словаре элемент
my_dict['Familia']=123
#и выводим его на экран
print("Элемент словаря  изначально отсутствовавший:")
print("my_dict[Familia] = ", end='')
print(my_dict['Familia'])

#Добавляем в словарь my_dict еще две пары
my_dict.update({'New_element':99999,'New_element2':6666})
# и проверяем, что получилось в словаре my_dict:
print("Наш словарь my_dict с новыми элементами: ",end='')
print(my_dict)

# А теперь из словаря my_dict удаляем одну из пар и выводим на экран значение этой пары
del my_dict['Name1']
#Теперь смотрим  значение удаленного элемента. Т,к.  его может не быть, на этот случай пишем комм-рий
print("Ищем удаленный элемент: ")
print(my_dict.get('Name1', "Увы, нету таких (вы их удалили)  :("))

#Выводим словарь на экран в окончательном виде
print("Наш словарь в окончательном виде my_dict: ",end='')
print(my_dict)

#Работа с множествами
print()
print("Работа с множеством.")
#Создаем множество my_set и присвоим ей значения
my_set={10,10,2,3,123,123, True,(1,4,6)}
#Смотрим ее на экране
print("Множество my_set в начале: ", end='')
print(my_set)

#Добавляем в my_set новые элементы 90709, 1234
my_set.add(90709)
my_set.add(1234)

#Удаляем элемент 10
my_set.discard(10)

#Смотрим окончательное множество на экране
print("Множество my_set в конце: ", end='')
print(my_set)

print("Конец программы")