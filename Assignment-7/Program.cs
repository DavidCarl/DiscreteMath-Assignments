using System;

namespace Assignment_7 {
    class Program {
        static void Main(string[] args) {
            Account account = new Account();
            Boolean running = true;
            helpCommand();
            while(running){
                Console.WriteLine("\nWaiting for your input... \n");
                string command = Console.ReadLine();
                running = commandController(command.ToLower(), account);
            }
            Console.WriteLine("Thank you for today!");
        }

        static Boolean commandController(string command, Account account) {
            if(command == "deposit") {
                depositCommand(account);
            } else if(command == "withdraw") {
                withdrawCommand(account);
            } else if (command == "help") {
                helpCommand();
            } else if (command == "exit") {
                return false;
            }
            return true;
        }

        static void depositCommand(Account account) {
            Console.WriteLine("Please enter a amount you wish to deposit");
            double amount = Convert.ToDouble(Console.ReadLine());
            try {
                double balance = account.Deposit(amount);
                Console.WriteLine("You now have " + balance + " USD left!");
            }catch(BalanceException ex){
                Console.WriteLine(ex.Message);
            }
        }

        static void withdrawCommand(Account account) {
            Console.WriteLine("Please enter a amount you wish to withdraw");
            double amount = Convert.ToDouble(Console.ReadLine());
            try {
                double balance = account.Withdraw(amount);
                Console.WriteLine("You now have " + balance + " USD left!");
            }catch(BalanceException ex){
                Console.WriteLine(ex.Message);
            }
        }
        static void helpCommand() {
            Console.WriteLine("You can use the following commands!");
            Console.WriteLine(" - deposit");
            Console.WriteLine(" - withdraw");
            Console.WriteLine(" - help");
            Console.WriteLine(" - exit");
        }
    }
}
