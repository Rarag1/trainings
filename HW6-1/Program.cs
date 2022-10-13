/* Задача 41: Пользователь вводит с клавиатуры M чисел. 
Посчитайте, сколько чисел больше 0 ввёл пользователь.

0, 7, 8, -2, -2 -> 2

1, -7, 567, 89, 223-> 3 */

//Почему ответ 3?

Console.Write($"Введите количество чисел: ");
int.TryParse(Console.ReadLine(), out int M);
int[] arrayM = new int[M];

for (int i = 0; i < M; i++)
{
    Console.Write($"Ведите {i + 1} число: ");
    int.TryParse(Console.ReadLine(), out arrayM[i]);
}

Console.WriteLine();
Console.Write($"Вы ввели: ");
int result = 0;

foreach (var item in arrayM)
{
    Console.Write($"{item} ");
    if (item > 0)
        result++;
}

Console.WriteLine($"\nИз них положительных: {result}");