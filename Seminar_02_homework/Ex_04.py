# Ex_4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите 
# произведение элементов на указанных позициях. Позиции хранятся в отдельном списке
# (пример n=4, lst1=[4,-2,1,3] - список на основе n, а позиции элементов lst2=[3,1].

from random import randint

number = int(input("Введите количество элементов: "))

def rand_numb (x, y, z):
    list_temp = []
    for i in range(z):
        temp = randint(x, y)
        while temp in list_temp or temp == 0:
            temp = randint(x, y)
        list_temp.append(temp)
    return list_temp

# Рандомное заполнение списка элементами
list1 = rand_numb (-number, number, number)
print(f" Список элементов: \n{list1}")

# Рандомное заполнение списка позиций
list2 = rand_numb (1, number - 1, randint(1, number-1))
print(f"Список позиций: \n{list2}")

# Нахождение произведения чисел из первого списка, 
# стоящих на позициях из второго списка
multip = 1
for i in range(len(list1)):
    if i in list2:
        multip *= list1[i]
print(f"Произведение чисел на соответствующих позициях: \n{multip}")