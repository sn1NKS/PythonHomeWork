# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

        # Вариант 1
        
# Ticket = input("Номер билета: ")
# PartTicket1 = int(Ticket[0]) + int(Ticket[1]) + int(Ticket[2]);
# PartTicket2 = int(Ticket[3]) + int(Ticket[4]) + int(Ticket[5]);
# if (PartTicket1 == PartTicket2):
#     print('Билет счастливый!')
# else:
#     print('У Вас обычный билет')

        # Вариант 2
        
Ticket = input("Номер билета: ")
PartTicket1 = int(Ticket[0]) + int(Ticket[1]) + int(Ticket[2]);
PartTicket2 = int(Ticket[3]) + int(Ticket[4]) + int(Ticket[5]);
if ((PartTicket1 + PartTicket2) % 2 == 0):
    print('Билет счастливый!')
else:
    print('У Вас обычный билет')   

       # Вариант 3
       
# while (True):
#         s = input('Введите 6-значный номер билета: ')
#         if len(s) != 6:
#                 print(f'Число {s} не 6-ти значное')
#         else:
#             res1 = 0
#             res2 = 0
#         for i in range(len(s)//2):
#             res1 += int(s[i])
#             res2 += int(s[len(s)//2 + i])
#         if res1 == res2:
#             print(f'{s} счастливый номер')
#         else:
#             print(f'{s} не счастливый номер')

