/*Задача 64: Задайте значение N. Напишите программу, 
которая выведет все натуральные числа в промежутке от N до 1. Выполнить с помощью рекурсии.

N = 5 -> "5, 4, 3, 2, 1"
N = 8 -> "8, 7, 6, 5, 4, 3, 2, 1" */


Console.Write($"Введите число: ");
int.TryParse(Console.ReadLine(), out int N);

PrintNum(N, 1);

void PrintNum(int _start, int _end)
{
    if (_start >= _end)
    {
        Console.Write($"{_start} ");
        PrintNum(_start - 1, _end);
    }
}