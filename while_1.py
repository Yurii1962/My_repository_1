#Домашняя работа по уроку "Стиль кода часть II. Цикл While"
#Исходный список:
my_list=[42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

#определяем длину списка
len_list=len(my_list)
#счетчик элементов списка my_list
counter=0

while counter<=len_list:
	#Берем очередной элемент списка my_list(counter)
	number=my_list[counter]
	#Счетчик инкрементируем
	counter = counter+1
	#Анализ очередного элемента
	if number>0:
		#элемент полож-ный, печатаем его
		print(number)
	elif  number < 0:
		#элемент отрицательный, выходим из while
		break

