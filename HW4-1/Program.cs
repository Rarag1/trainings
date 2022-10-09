int num = new Random().Next() % 10;
int degree = new Random().Next(1, 10);

int result = Degrees(num, degree);
Console.WriteLine($"Чило {num} в степени {degree} = {result}");

int Degrees(int _num, int _degree)
{
    int _result = _num;
    for (int i = 1; i < _degree; i++)
        _result = _result * _num;
    return _result;

}