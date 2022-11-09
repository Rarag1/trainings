/* Задача 58: Задайте две матрицы. Напишите программу, 
которая будет находить произведение двух матриц.
Например, даны 2 матрицы:
2 4 | 3 4
3 2 | 3 3
Результирующая матрица будет:
18 20
15 18 */

/*
C[0,0]=A[0,0]*B[0,0] + A[0,1]*B[1,0] + A[0,2]*B[2,0]
C[0,1]=A[0,0]*B[0,1] + A[0,1]*B[1,1] + A[0,2]*B[2,1]
C[1,0]=A[1,0]*B[0,0] + A[1,1]*B[1,0] + A[1,2]*B[2,0]
C[1,1]=A[1,0]*B[0,1] + A[1,1]*B[1,1] + A[1,2]*B[2,1]
*/

int[,] A = new int[2, 2]
{   {2, 4},
    {3, 2}};
int[,] B = new int[2, 2]
{   {3, 4},
    {3, 3}};
int[,] C = new int[A.GetLength(0), B.GetLength(1)];

if (A.GetLength(1) != B.GetLength(0))
    Console.Write($"Умножение невозможно");
else
{
    for (int i = 0; i < C.GetLength(0); i++)
    {
        for (int j = 0; j < C.GetLength(1); j++)
        {
            for (int k = 0; k < A.GetLength(1); k++)
            {
                C[i, j] += A[i, k] * B[k, j];
            }
        }
    }
}
PrintArray(C);


void PrintArray(int[,] _array)
{
    Console.WriteLine();
    for (int i = 0; i < _array.GetLength(0); i++)
    {
        for (int j = 0; j < _array.GetLength(1); j++)
            Console.Write($"{_array[i, j]}  ");
        Console.WriteLine();
    }
}