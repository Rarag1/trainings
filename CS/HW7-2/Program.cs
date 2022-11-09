/* Задача 50. Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, 
и возвращает значение этого элемента или же указание, что такого элемента нет.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
17 -> такого числа в массиве нет */

int[,] array1 = FillArray(5, 7);
Console.Write($"Введите позицию элемента: ");
int.TryParse(Console.ReadLine(), out int userNum);
int y = userNum / 10;
int x = userNum % 10;

/*Console.Write($"Ведите номер строки: ");
int.TryParse(Console.ReadLine(), out int y);
Console.Write($"Ведите номер столбца: ");
int.TryParse(Console.ReadLine(), out int x);*/

if (y <= array1.GetLength(0) && x <= array1.GetLength(1))
{
    Console.Write($"В массиве в {y} строке в {x} столбце находится число: {array1[y - 1, x - 1]} ");
}
else
    Console.WriteLine($"Такой ячейки в массиве нет ");


int[,] FillArray(int m, int n)
{
    int[,] array1 = new int[m, n];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            array1[i, j] = new Random().Next(-10, 10);
            Console.Write($"{array1[i, j]}  ");
        }
        Console.WriteLine();
    }
    return array1;
}