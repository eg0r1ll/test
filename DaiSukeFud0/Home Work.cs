static int Factorial(int n)
{
    if (n <= 0)
        return 1;
    else
        return n * Factorial(n - 1);
}
static int Pasled(int n)
{
    if (n == 1 || n == 2 || n == 3)
        return 1;
    else
        return Pasled(n - 1) + Pasled(n - 2) + Pasled(n - 3);
}
static Random rnd = new Random();
static int[] Arr_Random(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = rnd.Next(50);
    }
    return arr;
}
static void Array(int[] arr, int i = 0)
{
    Arr_Random(arr);
    if (i == arr.Length)
        return;
    Console.WriteLine($"Элемент {i} = " + arr[i]);
    Array(arr, i + 1);
}
static int SumFromAToB(int a, int b)
{
    if (a > b)
    {
        int temp = a;
        a = b;
        b = temp;
    }

    return (a + b) * (b - a + 1) / 2;
}
static void Main(string[] args)
{
    int[] arr = new int[10];
    Console.WriteLine("Факториал: " + Factorial(10));
    Console.WriteLine("Последовательность: " + Pasled(8));
    Array(arr);
    Console.Write("Введите начальное число: ");
    int start = int.Parse(Console.ReadLine());
    Console.Write("Введите конечное число: ");
    int end = int.Parse(Console.ReadLine());
    Console.WriteLine($"Сумма чисел от {start} до {end} = {SumFromAToB(start, end)}");