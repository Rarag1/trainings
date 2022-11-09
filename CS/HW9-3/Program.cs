/* Задача 68: Напишите программу вычисления функции Аккермана с помощью рекурсии. 
Даны два неотрицательных числа m и n.
m = 2, n = 3 -> A(m,n) = 9
m = 3, n = 2 -> A(m,n) = 29 */

Console.Write($"Введите m: ");
int.TryParse(Console.ReadLine(), out int m);
Console.Write($"Введите n: ");
int.TryParse(Console.ReadLine(), out int n);
Console.Write($"m = {m}, n = {n} -> A(m,n) = {Akkerman(m, n)}");

int Akkerman(int _m, int _n)
{
    if (_m == 0 && _n > 0) return _n + 1;
    else if (_m > 0 && _n == 0) return Akkerman(_m - 1, 1);
    else if (_m > 0 && _n > 0) return Akkerman(_m - 1, Akkerman(_m, _n - 1));
    else return -1;
}