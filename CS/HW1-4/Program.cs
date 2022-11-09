Console.Write("Введите число: ");
int.TryParse(Console.ReadLine(), out int N);
int num = 1;
while (num <= N)
{
    if (num % 2 == 0)
    {
        Console.Write($"{num} ");
    }
    num += 1;
}