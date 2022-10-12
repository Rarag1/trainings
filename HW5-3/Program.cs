/* Задача 38: Задайте массив вещественных чисел. 
Найдите разницу между максимальным и минимальным элементов массива.
[3 7 22 2 78] -> 76 */

int[] array1 = CreateAndPrintArray();
int max = array1[0], min = array1[0];
foreach (int i in array1)
{
    if (i > max)
        max = i;
    else if (i < min)
        min = i;
}
Console.WriteLine($"Разница между максимальным и минимальным значением элементов массива равна: {max - min}");


int[] CreateAndPrintArray()
{
    Console.Write($"Задайте длину массива: ");
    int.TryParse(Console.ReadLine()!, out int _size);
    int[] _array = new int[_size];
    for (int i = 0; i < _size; i++)
    {
        _array[i] = new Random().Next() % 100;
        Console.Write($"{_array[i]} ");
    }
    Console.WriteLine();
    return _array;
}