/* Задача 60. ...Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. 
Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
Массив размером 2 x 2 x 2
66(0,0,0) 25(0,1,0)
34(1,0,0) 41(1,1,0)
27(0,0,1) 90(0,1,1)
26(1,0,1) 55(1,1,1) */


int[,,] array1 = new int[2, 2, 2];

List<int> nums = new List<int>();

for (int i = 0; i < 90; i++)
    nums.Add(i + 10);

for (int i = 0; i < array1.GetLength(0); i++)
{
    for (int j = 0; j < array1.GetLength(1); j++)
    {
        for (int k = 0; k < array1.GetLength(2); k++)
        {
            int temp = new Random().Next(nums.Count);
            array1[i, j, k] = nums[temp];
            nums.RemoveAt(temp);
            Console.Write($"{array1[i, j, k]}({i},{j},{k}) ");
        }
        Console.WriteLine();
    }
}