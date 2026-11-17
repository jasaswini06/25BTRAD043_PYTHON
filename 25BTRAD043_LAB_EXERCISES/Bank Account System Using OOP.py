class BankAccount:

    def __init__(self, acc_no, holder_name, balance=0.0):
        self.acc_no = acc_no
        self.holder_name = holder_name
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ₹{amount:.2f} | Balance: ₹{self._balance:.2f}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self._balance:
            print("Transaction Failed: Insufficient balance!")
        else:
            self._balance -= amount
            print(f"Withdrawn: ₹{amount:.2f} | Balance: ₹{self._balance:.2f}")

    def check_balance(self):
        print(
            f"Account: {self.acc_no} ({self.holder_name}) | Balance: ₹{self._balance:.2f}"
        )


account = BankAccount("AC101", "Alex", 1000.0)

while True:
    print("\n1. Deposit  2. Withdraw  3. Check Balance  4. Exit")
    ch = input("Enter choice: ").strip()
    if ch == "1":
        account.deposit(float(input("Amount to deposit: ")))
    elif ch == "2":
        account.withdraw(float(input("Amount to withdraw: ")))
    elif ch == "3":
        account.check_balance()
    elif ch == "4":
        break
    else:
        print("Invalid choice.")