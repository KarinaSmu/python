# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую неотрицательную степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

print("Введите число")
a = int(input())
print("Введите степень")
b = int(input())

def num_exp(a, b):
    string="выражение не имеет смысла"
    if b==0 and a==0: return (string)
    elif b == 0: return (1)
    elif b == 1: return (a)
    else: return a*(num_exp (a, b-1))

print(num_exp (a, b))
   

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

print("Введите первое число")
c = int(input())
print("Введите второе число")
d = int(input())

def num_sum(a, b):
    if b == 0: return (a)
    else: return (num_sum (a+1, b-1))

print(num_sum (c, d))
