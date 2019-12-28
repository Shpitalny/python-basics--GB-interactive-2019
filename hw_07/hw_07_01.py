"""
1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.

Примечание: Списки фруктов создайте вручную в начале файла.

"""

fruits_list_1 = ['apple', 'orange', 'banana', 'lime']
fruits_list_2 = ['lime', 'mango', 'orange', 'pineapple']

fruits_intersection_2 = [fruit for fruit in fruits_list_1 if fruit in fruits_list_2]
print(fruits_intersection_2)
