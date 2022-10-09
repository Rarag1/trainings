Console.Write($"Введите число равное 8 =)): ");
int.TryParse(Console.ReadLine(), out int num);

CreateArray(num);

int[] CreateArray(int _num)
{
    int[] _array = new int[_num];
    for (int i = 0; i < _num; i++)
    {
        _array[i] = new Random().Next() % 100;
        Console.Write($"{_array[i]} ");
    }
    return _array;
}