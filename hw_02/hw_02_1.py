'''
Даны два произвольные списка.
Удалите из первого списка элементы присутствующие во втором списке.

'''

source_list = [2, 2, 2, 2, 2, 5, 5, 8, 2, 12, 12, 4]
excess_list = [2, 7, 12, 3]

source_list = [i for i in source_list[:] if i not in excess_list]
print(source_list)
