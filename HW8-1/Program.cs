/* Задача 54: Задайте двумерный массив. Напишите программу, 
которая упорядочит по убыванию элементы каждой строки двумерного массива.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
В итоге получается вот такой массив:
7 4 2 1
9 5 3 2
8 4 4 2 */

double[,] array1 = FillArray(3, 4);

for (int i = 0; i < array1.GetLength(0); i++)
{
    for (int j = 0; j < array1.GetLength(1); j++)
    {
        for (int t = 0; t < array1.GetLength(1); t++)
        {
            double temp = array1[i, t];
            if (array1[i, j] > temp)
            {
                temp = array1[i, j];
                array1[i, j] = array1[i, t];
                array1[i, t] = temp;
            }
        }
    }
}

PrintArray(array1);


double[,] FillArray(int m, int n, int k = 100)
{
    double[,] _array = new double[m, n];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            _array[i, j] = new Random().Next(-10 * k, 10 * k) / (double)k;
            Console.Write($"{_array[i, j]}  ");
        }
        Console.WriteLine();
    }
    return _array;
}

void PrintArray(double[,] _array)
{
    Console.WriteLine();
    for (int i = 0; i < array1.GetLength(0); i++)
    {
        for (int j = 0; j < array1.GetLength(1); j++)
        {
            Console.Write($"{_array[i, j]}  ");
        }
        Console.WriteLine();
    }
}