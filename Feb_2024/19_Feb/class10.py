class Payments:
    payment_mode = None
    password = None
    amount = None

    def payment_login(self):
        if self.password == 'password123':
            print('login is sucessful')
        else:
            print('login failed')

    def transaction(self):
        if self.amount == 100:
            print(f'Transaction is sucessful through {self.payment_mode}')
        else:
            print('Transaction failed')


google_pay = Payments()
google_pay.payment_mode = "Google Pay"
google_pay.password = input("enter the google pay password :")
google_pay.payment_login()
google_pay.amount = int(input("Enter the amount to be paid:"))
google_pay.transaction()


phonepe = Payments()
phonepe.payment_mode = "phonepe"
phonepe.password = input("enter the phonepe password :")
phonepe.payment_login()
phonepe.amount = int(input("Enter the amount to be paid:"))
phonepe.transaction()