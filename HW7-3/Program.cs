/* Задача 52. Задайте двумерный массив из целых чисел. 
Найдите среднее арифметическое элементов в каждом столбце.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3. */

int[,] array1 = FillArray(4, 5);
double result = 0;

Console.Write($"\n Среднее арифметическое каждого столбца: ");
for (int j = 0; j < array1.GetLength(1); j++)
{
    double sum = 0;
    for (int i = 0; i < array1.GetLength(0); i++)
    {
        sum += array1[i, j];
        result = Math.Round(sum / array1.GetLength(0), 2);
    }
    Console.Write($"{result}; ");
}

int[,] FillArray(int m, int n)
{
    int[,] array1 = new int[m, n];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            array1[i, j] = new Random().Next(0, 10);
            Console.Write($"{array1[i, j]}  ");
        }
        Console.WriteLine();
    }
    return array1;
}