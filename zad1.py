# Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("Введите число "))
suma = 0
while number > 0:
    a = number % 10
    suma = suma + a
    number = number // 10
print("Сумма чисел числа равна ", suma)
