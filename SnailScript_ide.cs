using System;
using System.Formats.Asn1;

class main_programm
{
    public static void funcntion_main(char[] args)
    {
        Console.WriteLine("Welcome to the SnailScriptIDE. What is on the Agenda today?");
        var function_main32 = new database();
        function_main32.load_database();

        string Type_of_file_ext = ".ss";
        string NameOfFile = Console.ReadLine();
        string name;
        if (NameOfFile == name)
        {
            Console.WriteLine("You file Name is:" + name);
            Console.WriteLine("You can start coding, without errors, and no error messages")

            string Coding_Interface = Console.ReadLine();
            Console.WriteLine("Your code: " + Coding_Interface);

            function_main32.load_system();
            function_main32.load_function_sys();
        }
    }
}

class secondary_program : main_program
{
    public static readonly void Start()
    {
        // Initialize background processes
        // Create background_proc variable in var typeword
        var background_proc = new Proc();
        background_proc.Init_all_background_procceses();

        background_proc.init_all_functions();
    }

    private static readonly void Main_end()
    {
        return 0;
    }
}
