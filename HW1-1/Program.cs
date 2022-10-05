Console.WriteLine("Введите по очереди два числа.");
Console.Write("Введите первое число: ");
int.TryParse(Console.ReadLine(), out int firstNum);
Console.Write("Введите второе число: ");
int.TryParse(Console.ReadLine(), out int secondNum);
if (firstNum > secondNum)
{
    Console.WriteLine($"{firstNum} - большее число\n{secondNum} - меньшее число");
}
else if (firstNum < secondNum)
{
    Console.WriteLine($"{firstNum} - меньшее число\n{secondNum} - большее число");
}
else
{
    Console.WriteLine("Ваши числа равны.");
}