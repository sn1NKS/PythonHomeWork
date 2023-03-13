# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# Форма записи 1
# Numbers = input("Введите трехзначное число: ")
# Numbers = int(Numbers)
 
# d1 = Numbers % 10
# Numbers = Numbers // 10
# d2 = Numbers % 10
# Numbers = Numbers // 10
 
# print("Сумма цифр числа:", Numbers + d1 + d2)

# Форма записи 2
Numbers = int(input("Введите трехзначное число: "))
 
d1 = Numbers % 10
Numbers = Numbers // 10
d2 = Numbers % 10
Numbers = Numbers // 10
 
print("Сумма цифр числа:", Numbers + d1 + d2)