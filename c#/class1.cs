using System;

namespace ClassLibrary1
{
    public static class Library
    {
        static public void test_function()
        {
            Console.WriteLine("Проверка работы");
        }
        static public double MinAVG(string[] marks)
        {
            double[] mass = new double[marks.Length];
            double sum = 0;

            for (int i = 0; i < marks.Length; i++)
            {
                Console.WriteLine(marks[i]);
                sum += Convert.ToDouble(marks[i]);
            }
            double minavg = sum / mass.Length;
            Console.WriteLine("minavg = " + minavg);
            return 0;
        }

    }
}
