class BankAccount:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        print(f"You withdrew {amount} EUR from account {self.acc_num}.")

    def balance_status(self, account_name):
        n = int((24-len(account_name))/2)
        n_right = n+1 if len(account_name) + 2*n != 24 else n
        print(f"{"-" * n}{account_name}{"-" * n_right}")
        print(f"| {"Account":10}{"Balance":>10} |")
        print(f"| {self.acc_num:<10}{self.balance:>10} |")
        print(f"{"-" * 24}")

    def menu(self):
        print("1: Withdraw\n"
              "2: Deposit\n")


class SavingsAccount(BankAccount):
    def __init__(self, acc_num, balance, saving_balance, interest_rate):
        super().__init__(acc_num, balance)
        self.interest_rate = interest_rate
        self.saving_balance = saving_balance

    def withdraw(self, amount, fee):
        self.saving_balance -= (amount + fee)

    def balance_status(self, account_name):
        n = int((38-len(account_name))/2)
        n_right = n+1 if len(account_name) + 2*n != 38 else n
        print(f"{"-" * n}{account_name}{"-" * n_right}")
        print(f"| {"Account":<10}{"Balance":>10}{"Savings":>14} |")
        print(f"| {self.acc_num:<10}{self.balance:>10}{self.saving_balance:>14} |")
        print(f"{"-" * 38}")

    def menu(self):
        print("1: Withdraw\n"
              "2: Deposit\n"
              "3: Withdraw from savings\n"
              "4: Deposit to savings\n"
              )
