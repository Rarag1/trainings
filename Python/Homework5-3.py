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