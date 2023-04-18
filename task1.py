"""Составить алгоритм: если введенное число больше 7, то вывести 'Привет'"""


def task():
    try:
        a = int(input())
        if a > 7:
            print('Привет')
        else:
            print('Слишком маленькое число')
            task()
    except ValueError:
        print('Введите числовой тип данных')
        task()


task()
