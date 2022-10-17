/*Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, 
которая будет находить строку с наименьшей суммой элементов.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
5 2 6 7
Программа считает сумму элементов в каждой строке
и выдаёт номер строки с наименьшей суммой элементов: 1 строка */

int[,] array1 = FillArray(4, 4);
List<int> sums = new List<int>();

for (int i = 0; i < array1.GetLength(0); i++)
{
    int sum = 0;
    for (int j = 0; j < array1.GetLength(1); j++)
        sum = sum + array1[i, j];
    sums.Add(sum);
}

Console.WriteLine();
int min = sums[0];
int iMin = 0;

for (int i = 0; i < sums.Count; i++)
{
    if (sums[i] < min)
    {
        min = sums[i];
        iMin = i;
    }
}
Console.Write($"Наименьшая сумма элементов ({min}) в строке с индексом : {iMin} \nОна же строка № {iMin + 1} ");


int[,] FillArray(int m, int n)
{
    int[,] _array = new int[m, n];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            _array[i, j] = new Random().Next(10);
            Console.Write($"{_array[i, j]}  ");
        }
        Console.WriteLine();
    }
    return _array;
}