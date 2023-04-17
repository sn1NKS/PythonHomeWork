# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A i.
# Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

Numbers = int(input("Общее количество элеметов: "));
list_1 = [];
for i in range(1, Numbers + 1):
    NumbersArray = int(input("Введите число: "))
    list_1.append(NumbersArray)
print(list_1);
Numbers2 = int(input("Введите величину: "));
result = 0;
for i in range(Numbers):
    if Numbers2 >= list_1[i]:
       result = max(list_1);
    else:
        Numbers2 <= list_1[i]
        result = min(list_1);
print(result);