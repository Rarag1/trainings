Console.Write($"Введите число: ");
int.TryParse(Console.ReadLine(), out int num);
Console.WriteLine($"Сумма цифр числа {num} = {Sumnum(num)}");

int Sumnum(int _num)
{
    _num = Math.Abs(_num);
    int _sumnum = 0;
    while (_num > 0)
    {
        _sumnum = _sumnum + _num % 10;
        _num = _num / 10;
    }
    return _sumnum;
}