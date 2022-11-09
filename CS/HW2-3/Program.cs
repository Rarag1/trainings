int dayOfTheYear = new Random().Next() % 366;
// допустим дни кратные 6 - субботы, кратные 7 - воскресенья (выходные), 1 число -понедельник.
if (dayOfTheYear % 6 == 0 || dayOfTheYear % 7 == 0)
{
    Console.WriteLine($"Сегодня {dayOfTheYear} день в году - Выходной");
}
else
{
    Console.WriteLine($"Сегодня {dayOfTheYear} день в году - Arbeiten!!!");
}