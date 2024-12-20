#Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else
#Задача "Все ли равны?"

#Ввод трех чисел
first=input("Ввести первое число: ")
second=input("Ввести второе число: ")
third=input("Ввести третье число: ")

if (first==second and second==third and third == first):
    print("ТРИ одинаковых")
elif(first==second):
    print("ДВА одинаковых")
elif(second==third):
    print("ДВА одинаковых")
elif(third==first):
    print("ДВА одинаковых")
else:print("НОЛЬ одинаковых")