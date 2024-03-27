class BankAccount:
    balance: int

    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def deposit(self, amount):
        self.balance = + amount
    def _withdraw(self, amount):
        self.balance = - amount
        print("withdraw")
    def __show_balance(self):
        print('your balance is ', self.balance)
    def if_you_are_auth(self, flag):
        if flag:
            self.__show_balance()
        else :
            print("Not allowed")
    def do_with_by_bank_manager(self, amount):
        self._withdraw(amount)
    def public_fn(self):
        print(self.__private_var)

jp_chase = BankAccount()
jp_chase.deposit(1000)
jp_chase.do_with_by_bank_manager(500)
jp_chase.if_you_are_auth(True)
jp_chase.public_fn()
jp_chase._withdraw(100)