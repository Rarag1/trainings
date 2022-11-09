/* Задача 43: Напишите программу, 
которая найдёт точку пересечения двух прямых, 
заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; 
значения b1, k1, b2 и k2 задаются пользователем.

b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; -0,5) */

/*  k1*x+b1 = k2*x+b2
    k1*x-k2*x = b2-b1
    x = (b2-b1)/(k1-k2)
    y = k1*x+b1
    x = (4-2)/(5-9) = 2/-4 = -0.5, y = 5*-0.5+2 = -0.5
*/

Console.WriteLine($"Введите коэффициенты для уравнений: y = k1 * x + b1, y = k2 * x + b2");
Console.Write($"b1 = ");
double.TryParse(Console.ReadLine(), out double b1);
Console.Write($"b2 = ");
double.TryParse(Console.ReadLine(), out double b2);
Console.Write($"k1 = ");
double.TryParse(Console.ReadLine(), out double k1);
Console.Write($"k2 = ");
double.TryParse(Console.ReadLine(), out double k2);
double x = (b2 - b1) / (k1 - k2);
double y = k1 * x + b1;
Console.WriteLine($"Прямые пересекутся в точке с координатами ({x},{y})");
