# Ex_5. Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)

from random import randint

number = int(input("Введите количество элементов: "))

# Создание списка элементов
list1 = []
for i in range(1, number + 1):
    list1.append(i)
print(f"Исходный список: \n{list1}")

# Рандомное перемешивание списка
list2 = []
for i in range(len(list1)):
    temp = list1[randint(0, len(list1) - 1)]
    while temp in list2:
        temp = list1[randint(0, len(list1) - 1)]
    list2.append(temp)
print(f"Результат перемешивания: \n{list2}")