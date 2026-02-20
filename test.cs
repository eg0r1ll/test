using System;

namespace Program
{
	class Programm
	{
		static void Main()
		{
			int[,] array = new int[6, 5];
			Random rand = new Random();
			int sum_1 = 0;

			// Заполнение массива:
			for(int i = 0; i < array.GetLength(0); ++i)
			{
				for (int j = 0; j < array.GetLength(1); ++j)
				{
					array[i, j] = rand.Next(1, 5);
					sum_1 += array[i, j];
				}
			}

			// Вывод массива и суммы строк
			for(int i = 0; i < array.GetLength(0); ++i)
			{
				int temp_sum = 0;
				for(int j = 0; j < array.GetLength(1); ++j)
				{
					temp_sum += array[i, j];
					
					if (j == array.GetLength(1) - 1)
					{
						
						Console.Write($"{array[i, j]}\t{temp_sum}");
						continue;
					}
					
					Console.Write($"{array[i, j]}\t");
				}
				Console.WriteLine();
			}

			// Вывод суммы столбцов:
			Console.WriteLine();
			for(int i = 0; i < array.GetLength(1); ++i)
			{
				int temp_sum = 0;
				for (int j = 0; j < array.GetLength(0); ++j)
				{
					temp_sum += array[j, i];
				}
				Console.Write($"{temp_sum}\t");
			}		
			
			Console.WriteLine(sum_1); // Вывод суммы всех значений массива
		}
	}
}
