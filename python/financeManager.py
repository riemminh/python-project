import json
import os
from enum import Enum


class Choice(Enum):
    ADD_INCOME = 1
    ADD_EXPENSE = 2
    SHOW_REPORT = 3
    SHOW_BALANCE = 4
    EXIT = 5

class Transaction:
    def __init__(self, type, amount, description):
        self.type = type
        self.amount = amount
        self.description = description

    def to_dict(self):
        return {"type": self.type, "amount": self.amount, "description": self.description}

    @classmethod
    def from_dict(cls, data):
        return cls(data["type"], data["amount"], data["description"])

    def __str__(self):
        return f"Type: {self.type.capitalize()}, Amount: {self.amount}, Description: {self.description}"

class FinanceManager:
    def __init__(self, filename="finance.json"):
        self.filename = filename
        self.transactions = self.load_transactions()

    def load_transactions(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [Transaction.from_dict(transaction) for transaction in data]
        return []

    def save_transactions(self):
        with open(self.filename, "w") as f:
            json.dump([transaction.to_dict() for transaction in self.transactions], f, indent=4)

    def add_income(self, amount, description):
        transaction = Transaction("income", amount, description)
        self.transactions.append(transaction)
        self.save_transactions()

    def add_expense(self, amount, description):
        transaction = Transaction("expense", amount, description)
        self.transactions.append(transaction)
        self.save_transactions()

    def get_balance(self):
        balance = 0
        for transaction in self.transactions:
            if transaction.type == "income":
                balance += transaction.amount
            elif transaction.type == "expense":
                balance -= transaction.amount
        return balance

    def show_report(self):
        if not self.transactions:
            print("No transactions found.")
        for transaction in self.transactions:
            print(transaction)

def main():
    manager = FinanceManager()

    while True:
        print("\nPersonal Finance Management System")
        print(f"{Choice.ADD_INCOME.value}. Add Income")
        print(f"{Choice.ADD_EXPENSE.value}. Add Expense")
        print(f"{Choice.SHOW_REPORT.value}. Show Transaction Report")
        print(f"{Choice.SHOW_BALANCE.value}. Show Current Balance")
        print(f"{Choice.EXIT.value}. Exit")

        try:
            choice = int(input("Enter choice: "))
            if choice not in [Choice.ADD_INCOME.value, Choice.ADD_EXPENSE.value, Choice.SHOW_REPORT.value, Choice.SHOW_BALANCE.value, Choice.EXIT.value]:
                print("Invalid choice, please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == Choice.ADD_INCOME.value:
            amount = float(input("Enter income amount: "))
            description = input("Enter description: ")
            manager.add_income(amount, description)
            print("Income added successfully!")
        elif choice == Choice.ADD_EXPENSE.value:
            amount = float(input("Enter expense amount: "))
            description = input("Enter description: ")
            manager.add_expense(amount, description)
            print("Expense added successfully!")
        elif choice == Choice.SHOW_REPORT.value:
            manager.show_report()
        elif choice == Choice.SHOW_BALANCE.value:
            balance = manager.get_balance()
            print(f"Current Balance: {balance}")
        elif choice == Choice.EXIT.value:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
