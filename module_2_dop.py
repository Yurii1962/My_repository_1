"""Дополнительное задание к модулю 2
Вводится  произвольное число number. Надо найти
все сочетания двух чисел,
сумме которых кратно number.
Напр., для 9 это будут 1+2,1+8,2+7,3+6,4+5 """
number = int(input("Ввести число от 3 до 20: "))
string_password=''  #в эту строку собираем найденные числа
for i in range(1, number):
    for j in range((i+1), (number + 1)):
        if ((number % (i+j)) == 0):
            string_password=string_password+str(i)+str(j)
print(f" Для введенного числа {number} string = ", string_password)

