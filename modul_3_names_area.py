#ДЗ по уроку "Пространство имен"
#Задача "Счетчик вызовов"

#Глобальная переменная, счетчик вызовов функций
calls = 0

#Функция count_calls, подсчитывает вызовы других ф-ий
def count_calls():
    global calls
    calls += 1
    return

#Функция string_info. Принимает строку "а" и возвращает
# кортеж = длина строки len_a, строка в верхнем регистре up_a,
# строка в нижнем р-ре up_a
def string_info(a):
    count_calls()
    len_a = len(a)  #длина строки
    up_a = a.upper()    #строка в верхнем р-ре
    down_a = a.lower()  #строка в нижнем р-ре

    #делаем кортеж из полученных элементов
    corteg = (len_a, up_a, down_a)
    return corteg

#Функция is_contains. Принимает строку "a" и список "b". Возвращает True,
# если строка "a" входит в список "b", иначе - False
def is_contains(a, b):
    count_calls()
    #Строку "a" переводим в нижий индекс
    a = a.lower()
    # Перевести элементы списка "b" в нижний индекс
    # длина списка
    dl = len(b)
    for i in range(dl):
        str = b[i]
        str = str.lower()
        b[i] = str

    if (a in b):
        exist = True
    else: exist = False
    return exist

#Тестовые данные
s1 = "Capybara"
s2 = "Armageddon"

b1 = "Urban"
l1 = ["ban", "BaNaN", "urBAN"]

b2 = "cycle"
l2 = ["recycling", "cyclic"]

#вызовы ф-ций с тестовыми данными

print(string_info(s1))
print(string_info(s2))

print(is_contains(b1, l1))
print(is_contains(b2, l2))

print("Кол-во вызовов функций = ", calls)