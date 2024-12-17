# Задача "Рекурсивное умножение цифр":
#
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа.
#
#
# Пункты задачи:
#
#     1. Напишите функцию get_multiplied_digits и параметр number в ней.
#     2. Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
#     3. Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите
#        в неё первый символ из str_number в числовом представлении(int).
#     4. Возвращайте значение first * get_multiplied_digits(int(str_number[1:])). Таким образом
#        вы умножите первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры.
#     5. Пункт 4 можно выполнить только тогда, когда длина str_number больше 1, т.к. в противном случае
#        не получиться взять срез str_number[1:].
#     6. Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.
#
# Стек вызовов будет выглядеть следующим образом:
#
# get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3

def get_multiplied_digits(number):
    str_number = str(int(number))
    if len(str_number) <= 1:
        return int(str_number)
    else:
        first_digit = int(str_number[0])
        rest_digits = int(str_number[1:])
        if rest_digits == 0:
            return first_digit
        else:
            return first_digit * get_multiplied_digits(rest_digits)


print(get_multiplied_digits(1234))
print(get_multiplied_digits(1020304))
print(get_multiplied_digits(100200300400))
print(get_multiplied_digits(1000200030004000))
