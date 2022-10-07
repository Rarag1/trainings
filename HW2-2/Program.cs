Console.Write("Введите число: ");
int.TryParse(Console.ReadLine(), out int num);
if (num / 100 == 0)
{
    Console.WriteLine("третьей цифры нет");
}
else
{
    while (num / 1000 != 0)
    {
        Console.WriteLine(num = num / 10);
    }
    Console.WriteLine($"Третья цифра: {num % 10}");
}