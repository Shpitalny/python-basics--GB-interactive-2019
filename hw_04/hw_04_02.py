'''
2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

'''

def my_max(*args):
    max_ = args[0]
    for e in args[1:]:
        if max_ < e:
            max_ = e
    return max_

print(my_max(1, 5, 3))
