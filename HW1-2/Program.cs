Console.WriteLine("Введите по очереди три числа.");
Console.Write("Введите первое число: ");
int.TryParse(Console.ReadLine(), out int firstNum);
Console.Write("Введите второе число: ");
int.TryParse(Console.ReadLine(), out int secondNum);
Console.Write("Введите третье число: ");
int.TryParse(Console.ReadLine(), out int thirdNum);
int max = firstNum;
if (secondNum > max)
{
    max = secondNum;
}
if (thirdNum > max)
{
    max = thirdNum;
}
Console.WriteLine(max);