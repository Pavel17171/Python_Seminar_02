#Ex_3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

number = int(input("Введите количество элементов: "))
list_1 = []
sum_numbers = 0
for n in range(1, number + 1):
    temp = (1 + 1 / n) ** n
    list_1.append(temp)
    sum_numbers += temp
print(sum_numbers)