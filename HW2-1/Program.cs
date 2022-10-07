int num = new Random().Next() % 900 + 100;
Console.WriteLine($"В числе {num} вторая цифра: {((num % 100) / 10)}");