using System;

namespace Assignment_7{
    class BalanceException : Exception {
        public BalanceException() {
        }

        public BalanceException(string message) : base(message) {
        }
    }
}