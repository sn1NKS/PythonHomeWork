# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

# Numbers = int(input("Общее количество элеметов: "));
# list_1 = [];
# for i in range(1, Numbers + 1):
#     list_1.append(i)
# print(list_1);
# Numbers2 = int(input("Выберите число: "));
# for i in list_1:
#     if Numbers2 in list_1:
#         print("Число присутствует")
#         break;
#     else:
#         print("Число отсутствует")
#         break;

# Решение с помощью функции count()
# Numbers = int(input("Общее количество элеметов: "));
# list_1 = [];
# for i in range(1, Numbers + 1):
#     NumbersArray = int(input("Введите число: "))
#     list_1.append(NumbersArray)
# print(list_1);
# Numbers2 = int(input("Выберите элемент из списка: "));
# if Numbers2 in list_1:
#         result = list_1.count(Numbers2);
# print(f"Количество повторов: {result}");

# Решение другого студента
# Number = abs(int(input('Введите количество элементов списка А: ')))
# A_entered = input("Введите через пробел элементы списка: ").split()
# A_num = list(map(int, A_entered))
# if len(A_num) != Number:
#     print('Введенные элементы не соответствуют заявленному количеству!')
# else:
#     X = int(input('Введите число X, которое необходимо найти в списке: '))
#     count = 0
#     for i in range(Number):
#         if A_num[i] == X:
#             count += 1
#     print(f'Число {X} встречается в списке A {count} раз') 

# Моё решение. 
Numbers = int(input("Общее количество элеметов: "));
list_1 = [];
for i in range(1, Numbers + 1):
    NumbersArray = int(input("Введите число: "))
    list_1.append(NumbersArray)
print(list_1);
Numbers2 = int(input("Выберите элемент из списка: "));
count = 0;
for i in range(Numbers):
    if Numbers2 == list_1[i]:
        count += 1;
print(f"Количество повторов: {count}");