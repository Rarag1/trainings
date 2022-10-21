/*Задача 66: Задайте значения M и N. Напишите программу, 
которая найдёт сумму натуральных элементов в промежутке от M до N.

M = 1; N = 15 -> 120
M = 4; N = 8. -> 30 */


Console.Write($"Введите начальное число: ");
int.TryParse(Console.ReadLine(), out int M);
Console.Write($"Введите конечное число: ");
int.TryParse(Console.ReadLine(), out int N);

if (M > N)
{
    int temp = M; M = N; N = temp;
}

Console.Write($"Сумма чисел между введенными значениями равна: {SumNum(M, N)} ");

int SumNum(int _start, int _end)
{
    if (_start == _end)
        return _end;
    else return _start + SumNum(_start + 1, _end);
}