"""Составить алгоритм:
если введенное имя совпадает с Вячеслав, то вывести “Привет, Вячеслав”, если нет, то вывести 'Нет такого имени'"""

inp = input()
if inp == 'Вячеслав':
    print('Привет, ' + inp)
else:
    print('Нет такого имени')
