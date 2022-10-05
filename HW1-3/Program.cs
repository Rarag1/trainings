Console.Write("Введите число: ");
int.TryParse(Console.ReadLine(), out int num);
if (num % 2 == 0)
{
    Console.WriteLine("Число четное.");
}
else
{
    Console.WriteLine("Число нечетное.");
}