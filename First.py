# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет


selectDay =int(input('Введите номер дня недели: '))
if 0 < selectDay < 6:
    print('Будний день')
elif 5<selectDay<8:
    print('Выходной день')
else:
    print('Дня недели с таким номером нет.')