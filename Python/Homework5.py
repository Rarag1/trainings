# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

string = "Клёпа абвалила рабвладение полность, сабврав все силы"
result = " ".join([e for e in string.split() if "абв" not in e])
print(result)


# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

total = 121
from random import randint
rang = randint(1,2)
while total > 0:
    if rang == 1:
        mov = int(input("Ходит первый игрок.\nВведите кол-во конфет от 0 до 28: "))
        if mov < 0 or mov >28: print("Некорректный ввод. Переход хода")
        else: total-= mov
        rang+=1
    else:
        # mov = int(input("Ходит второй игрок.\nВведите кол-во конфет от 0 до 28: "))
        mov = total % 29
        print("Ходит ИИ.\nБеру", mov, "конфет.")
        if mov < 0 or mov >28: print("Некорректный ввод. Переход хода")
        else: total-= mov   
        rang-=1
    if total > 0: print("\nОсталось", total,"конфет.")
if rang == 2:print("\nПобедил первый игрок.")
else: print("\nПобедил второй игрок (или ИИ).")


# Создайте программу для игры в ""Крестики-нолики"".

import numpy as np
from random import randint
A = np.zeros((4, 4))
print(A)

while True:
    if A[0,:].sum() == 4 or A[1,:].sum() == 4 or A[2,:].sum() == 4 or A[3,:].sum() == 4 or\
    A[:,0].sum() == 4 or A[:,1].sum() == 4 or A[:,2].sum() == 4 or A[:,3].sum() == 4 or\
    np.diag(A).sum() == 4 or np.diag(-A).sum() == 4:
        print("Выиграл 1-й игрок.")
        break
    elif A[0,:].sum() == 20 or A[1,:].sum() == 20 or A[2,:].sum() == 20 or A[3,:].sum() == 20 or\
    A[:,0].sum() == 20 or A[:,1].sum() == 20 or A[:,2].sum() == 20 or A[:,3].sum() == 20 or\
    np.diag(A).sum() == 20 or np.diag(-A).sum() == 20:
        print("Выиграл 2-й игрок.")
        break

    rang = randint(1,2) # добавлен фактор рандомного призового хода
    lucky = randint(0,1) # есть возможность перебивать занятую позицию, если удача с тобой
    if rang == 1:
        [i,j] = map(int, input("\nХодит 1-й игрок.\n\
Введите 2-е координаты (от 0 до 3) хода через запятую: ").split(","))
        if A[i,j] == 0: A[i,j] = 1
        elif A[i,j] != 0 and lucky !=0: A[i,j] = 1 
        print(A)
        print("lucky =", lucky)
        rang+=1
    else:
        [i,j] = map(int, input("\nХодит 2-ой игрок.\n\
Введите 2-е координаты (от 0 до 3) хода через запятую: ").split(","))
        if A[i,j] == 0: A[i,j] = 5
        elif A[i,j] != 0 and lucky !=0: A[i,j] = 5
        print(A)
        print("lucky =", lucky)
        rang-=1

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

data = "аааааааббббббббвввввввввггггг"
def rle_encode(data):
    encoded = ""
    prev_char = data[0]
    count = 0
    for char in data:
        if char == prev_char:count+=1
        else: 
            encoded += str(count) + prev_char
            prev_char = char
            count = 1          
    return encoded
data1 = rle_encode(data+" ")
print(rle_encode(data+" "))

def rle_decode(data):
    decoded = ""
    count = 0
    for char in data:
        if char.isdigit(): count = int(char)
        else: 
            decoded += char * count
            count = 0
    return decoded
print(rle_decode(data1))