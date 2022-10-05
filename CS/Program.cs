Console.Write("Введите число: ");
int.TryParse(Console.ReadLine(), out int x);
Console.WriteLine($"Квадрат введенного числа = {x * x}");
