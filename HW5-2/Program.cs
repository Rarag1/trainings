/* Задача 36: Задайте одномерный массив, заполненный случайными числами. 
Найдите сумму элементов, стоящих на нечётных позициях.
[3, 7, 23, 12] -> 19
[-4, -6, 89, 6] -> 0 */

int[] array1 = CreateAndPrintArray();
int sum = 0;
for (int i = 1; i < array1.Length; i += 2)
    sum = sum + array1[i];
Console.WriteLine($"Сумма элементов, стоящих на нечетных позициях равна: {sum}");

int[] CreateAndPrintArray()
{
    Console.Write($"Задайте длину массива: ");
    int.TryParse(Console.ReadLine()!, out int _size);
    int[] _array = new int[_size];
    for (int i = 0; i < _size; i++)
    {
        _array[i] = new Random().Next(-10, 10);
        Console.Write($"{_array[i]} ");
    }
    Console.WriteLine();
    return _array;
}
