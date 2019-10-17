using System;
using System.Diagnostics.Contracts;

namespace Assignment_7{
    class Account{
        double balance = 1000;

        public double Deposit(double amount) {
            Contract.Requires(amount > 0);
            Contract.Ensures(balance >= Contract.Result<double>());
            if (amount < 0) {
                throw new BalanceException("Its not possible to deposit a negativ number!");
            }
            balance += amount;
            return balance;
        }

        public double Withdraw(double amount) {
            Contract.Requires(amount > 0);
            Contract.Requires(amount <= balance);
            Contract.EnsuresOnThrow<Exception>(amount > balance);
            if (amount > balance) {
                throw new BalanceException("Its not possible to withdraw more money than you have! Your balance is " + balance);
            }
            balance -= amount;
            return balance;
        }
    }
}