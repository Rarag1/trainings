/* Задача 34:
Задайте массив заполненный случайными положительными трёхзначными числами. 
Напишите программу, которая покажет количество чётных чисел в массиве.

[345, 897, 568, 234] -> 2 */

int[] array1 = CreateAndPrintArray();
int count = 0;
foreach (int i in array1)
{
    if (i % 2 == 0)
        count++;
}
Console.WriteLine($"Количество четных чисел равно: {count}");


int[] CreateAndPrintArray()
{
    Console.Write($"Задайте длину массива: ");
    int.TryParse(Console.ReadLine()!, out int _size);
    int[] _array = new int[_size];
    for (int i = 0; i < _size; i++)
    {
        _array[i] = new Random().Next() % 900 + 100;
        Console.Write($"{_array[i]} ");
    }
    Console.WriteLine();
    return _array;
}