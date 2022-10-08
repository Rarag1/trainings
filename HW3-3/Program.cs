Console.Write("Введите положительное целое число N: ");
int.TryParse(Console.ReadLine(), out int N);
for (int i = 1; i <= N; i++)
{
    Console.Write($"{Math.Pow(i, 3)} ");
}