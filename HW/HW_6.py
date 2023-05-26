# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

print("Введите первый элемент прогрессии")
a1 = int(input())
print("Введите разность")
d = int(input())
print("Введите количество элементов")
n = int(input())

def arithprogres(a1,d,n):
     progres=[n]
     progres[0]=a1
     progres=[a1+(i-1)*d for i in range(1,n)]
     return progres
   
print(arithprogres(a1,d,n))


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
def indexsearch(array,min,max):
     newarray=[i for i in range(len(array)) if array[i]>=min and array[i]<=max]
     return newarray

print("Введите минимум")
min = int(input())
print("Введите максимум")
max = int(input())
array1=[random.randint(0,10) for i in range(20)]
print(array1)
print(indexsearch(array1,min,max))

# Ввожу какой то ненужный комментарий :)
