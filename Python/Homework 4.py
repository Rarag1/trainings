# Вычислить число c заданной точностью d.
# Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# формула Саймона Плаффа
d = int(input("Задайте точность: "))
pi = 0
for k in range(d):
    pi += (((1/16)**k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6)))
print(round(pi, d))


# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

N = int(input("Введите число: "))
result =[]
mult = 2
while mult <= N:
    if N % mult == 0:
        result.append(mult)
        N /= mult
    else: mult += 1
print(result)


# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

list1 = list(map(int, input("Введите список: ").split()))
list2 = []
for e in list1:
    if e not in list2:
        list2.append(e)
print(list1)
print(list2)


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input('Введите степень многочлена: '))
m = ""
for i in range(k):
    r = random.randint(1,10)
    if r !=0:
        m += str(r)+"x**"+str(k) + "+"
    k-=1
m += str(random.randint(0,100)) + "=0"
with open('Homwork4.txt', 'w') as HW:
    HW.writelines(m)


# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

with open('Homework4-1.txt', 'r') as HW4_1:
    data1 = list(map(int, HW4_1.readlines()))
with open('Homework4-2.txt', 'r') as HW4_2:
    data2 = list(map(int, HW4_2.readlines()))
# print(data1)
# print(data2)
minlen = len(data1)
min = data1
max = data2
if len(data1) > len(data2):
    minlen = len(data2)
    min = data2
    max = data1
data3 = max[:len(max)-len(min)]
# print(data3)
for i in range(minlen):
    data3.append(min[i] + max[len(max)-len(min) + i])
# print(data3)
with open('Homework4-3.txt', 'w') as HW4_3:
    data3 = list(map(str, data3))
    # print(data3)
    for e in data3:
        HW4_3.write(e)
        HW4_3.write('\n')