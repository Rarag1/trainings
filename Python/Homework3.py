# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
L1 = [2, 3, 5, 9, 3]
L2 = random.sample(range(100), 7)

def Sum(list):
    LR = list[1::2]
    print(list)
    print(LR, "->", sum(LR))
    return

Sum(L1)
Sum(L2)

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

L1 = [2, 3, 4, 5, 6]
L2= [2, 3, 5, 6]

def PowPar(list):
    LResult =[]
    j=-1
    for i in range(len(list)):
        while i < len(list)/2:
            LResult.append(list[i]*list[j])
            # print(i, j, LResult)
            i+=1; j-=1
        return LResult
  
print(PowPar(L1))
print(PowPar(L2))


# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import numpy as np
L1 = [1.1, 1.2, 3.1, 5, 10.01]
L2 = np.random.random_sample(size = 5)

def DiffDec(list):
    LRes=[]
    for elem in list:
        if round(elem%1, 3) != 0:
            LRes.append(round(elem%1, 3))
    print(list)
    print(LRes)
    print(max(LRes), "-", min(LRes), " = ", round(max(LRes)-min(LRes), 3))
    return  round(max(LRes)-min(LRes), 3)

DiffDec(L1)
DiffDec(L2)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n10 = int(input("Введите число: "))
n2 = ""
while n10 != 0:
    n2 = str(n10 % 2) + n2
    n10 = n10 // 2
print(n2)


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

N = int(input("Введите число: "))
def Fib(n):
    if n in [-1, 1, 2]:return 1
    elif n == 0: return 0
    elif n == -2: return -1
    elif n > 2: return Fib(n-1) + Fib(n-2)
    elif n < 2: return Fib(n+2) - Fib(n+1)

LF = []
for i in range(-N,N+1):
    LF.append(Fib(i))
print(LF)