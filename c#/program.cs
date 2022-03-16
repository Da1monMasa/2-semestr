using System;
using ClassLibrary1;
namespace ConsoleAppTest
{
    class Program
    {
       
        static void Main(string[] args)
        {
            string[] marks = { "3", "3", "4", "5"};

            Library.MinAVG(marks);
            Library.test_function();
            Console.WriteLine("Hello World!");
        }
       

    }
}
