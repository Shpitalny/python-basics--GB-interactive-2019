"""
3: Напишите функцию которая принимает на вход список.
Функция создает из этого списка новый список из квадратных корней чисел (если число положительное)
и самих чисел (если число отрицательное) и возвращает результат
(желательно применить генератор и тернарный оператор при необходимости).
В результате работы функции исходный список не должен измениться.

Например:
old_list = [1, -3, 4]
result = [1, -3, 2]
Примечание: Список с целыми числами создайте вручную в начале файла.
Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.

"""

from math import sqrt

def positive_sqrt(lst):
    return [n if n < 0 else sqrt(n) for n in lst]

rand_list = [-28, -21, -48, 3, -34, 42, 7, 38, 46, -6, 50, 34, -30, -17, -6, 46, -21, -31, -2, -40]
print(f'new list:\n{positive_sqrt(rand_list)}\n')
print(f'old list:\n{rand_list}')
