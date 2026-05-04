static Random random = new Random();
static int[] array1 = new int[10];
static int[] array2 = new int[10];
static int[] Filling_Array(int[] array)
{
    for (int i = 0; i < array.Length; i++)
        array[i] = random.Next(50);
    return array;
}
static int Sum(int[] array)
{
    int result = 0;
    foreach (int i in array)
        result += i;
    return result;
}
static double Coculation(double num1, double num2, char symbol)
{
    double result = 0;
    for (int i = 0; true; i++)
    {
        if (symbol == '+')
        {
            result = num1 + num2; break;
        }
        else if (symbol == '-')
        {
            result = num1 - num2; break;
        }
        else if (symbol == '*')
        {
            result = num1 * num2; break;
        }
        if (symbol == '/')
        {
            if (num2 != 0)
            {
                result = num1 / num2;
                break;
            }
            if (num2 == 0)
            {
                Console.WriteLine("На ноль делить нельзя");
                break;
            }
        }
    }
    return result;
}
static void Main(string[] args)
{
    Filling_Array(array1);
    Filling_Array(array2);
    Console.WriteLine($"Сумма элементов 1-го массива = {Sum(array1)}");
    Console.WriteLine($"Сумма элементов 2-го массива = {Sum(array2)}");
    while (true)
    {
        try
        {
            if (Sum(array1) > Sum(array2))
            {
                Console.Write("Введите 1 число: ");
                double num1 = double.Parse(Console.ReadLine());
                Console.Write("Введите 2 число: ");
                double num2 = double.Parse(Console.ReadLine());
                Console.Write("Выбирете операцию '-' '+' '/' '*': ");
                char symbol = char.Parse(Console.ReadLine());
                Console.WriteLine(Coculation(num1, num2, symbol));
                Console.Clear();
                Console.WriteLine("Для выхода нажмите Escape");
                Console.WriteLine("Чтобы продолжить нажмите Enter");
                ConsoleKey key = Console.ReadKey().Key;
                if (key == ConsoleKey.Escape)
                    break;
            }
            if (Sum(array2) > Sum(array1))
            {
                Console.WriteLine("Введите число 1-10");
                int num = int.Parse(Console.ReadLine());
                if (num % 2 == 0 && num != 0)
                {
                    Console.WriteLine($"Число {num} - четное"); break;
                }
                else if (num == 0)
                {
                    Console.WriteLine("Введите число 1-10"); break;
                }
                else if (num % 2 == 1)
                    Console.WriteLine($"Число {num} - нечетное");
                break;
            }
        }
        catch (Exception)
        {
            Console.WriteLine("Введите все правильно"); continue;
        }
    }