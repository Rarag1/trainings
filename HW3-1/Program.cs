Console.Write($"Введите пятизначное число: ");
int.TryParse(Console.ReadLine(), out int num);
//Console.WriteLine($" {num / 10000}, {num % 10}, {num % 10000 / 1000}, {num % 100 / 10}");
if ((num / 10000 == num % 10) && (num % 10000 / 1000 == num % 100 / 10))
{
    Console.WriteLine($"Число {num} - полиндром.");
}
else
{
    Console.WriteLine($"Число {num} - не полиндром.");
}