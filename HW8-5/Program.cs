/* Задача 62. Напишите программу, которая заполнит спирально массив 4 на 4.
Например, на выходе получается вот такой массив:
01 02 03 04
12 13 14 05
11 16 15 06
10 09 08 07 */


int[,] array1 = new int[4, 4];

for (int i = 0, j = 0, k = 10; k < array1.Length + 10; k++)
{
    array1[i, j] = k + 1;
    if (i <= j + 1 && i + j < array1.GetLength(1) - 1)
        j++;
    else if (i >= j && i + j > array1.GetLength(1) - 1)
        j--;
    else if (i < j)
        i++;
    else if (i > j)
        i--;
}
PrintArray(array1);

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