class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def showbalance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(
            f"Rs{amount} deposited successfully and your current balace is Rs{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Rs{amount} withdrawn from your account")


account = None

while True:
    print("1. Create account")
    print("2. Deposite Money")
    print("3. Withdraw Money")
    print("4. Show Balance")
    print("5. Exit")
    choice = int(input("What do you wanna do:"))

    if choice == 1:
        # creating account
        Full_name = input("Enter your full name:")
        while True:
            try:
                initial_balance = int(input("Enter intial balance:"))
                break
            except ValueError:
                print("Enter valid amount")

        account = BankAccount(Full_name, initial_balance)
        print(f"Account1 Created by the name: {Full_name}")
    elif choice == 2:
        # deposit
        if account is None:
            print("Please create an account")

        while True:
            try:
                amount = int(input("How much money want to deposit:"))
                account.deposit(amount)
                break
            except:
                print("Enter valid amount")
    elif choice == 3:
        if account is None:
            print("Please create an account!")

        while True:
            try:
                amount = int(input("Enter Withdraw amount:"))
                account.withdraw(amount)
                break
            except:
                print("Enter valid amount")
    elif choice == 4:
        if account is None:
            print("Please create an account first")
        else:
            print(f"Account Holder:Rs {account.name}")
            print(f"Current Balance: Rs{account.balance}")

    elif choice == 5:
        break
    else:
        print("Choose the number between 1-5")
        print("Invalid choice")
