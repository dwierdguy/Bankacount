import datetime
import pytz

class Bank(object):

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_time = []
        print(f'\nAccount created for {self.name} and credited with Rs.{self.balance}')

    def new_deposit(self, amount):
        try:
            if amount > 0:
                self.balance += amount
                date = datetime.date.today()
                time = datetime.time
                self.transaction_time.append((datetime.datetime.utcnow().strftime('%B %d %Y - %H:%M:%S'), amount, 1, self.balance))
                print(f'\nAccount credited with Rs.{amount} and new balance is Rs.{self.balance}')
            else:
                print('\nPlease provide cash more than Rs.0')
        except TypeError:
            pass

    def check_balance(self):
        print(f'Your account is left with : Rs.{self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print("You don't have enough cash")
        else:
            self.balance -= amount
            self.transaction_time.append((datetime.datetime.utcnow().strftime('%B %d %Y - %H:%M:%S'), amount, 0, self.balance))
            print(f'Your account is left with : {self.balance}')

    def statement(self):
        tran_time = ''
        transaction = ''
        for n in self.transaction_time:
            tran_time = n[0]
            transaction = n[1]
            credit = n[2]
            balance = n[3]
            if credit == 1:
                print(f"Date : {tran_time}, Amount Debited : Rs.{transaction}, New Balance : {balance}")
            else:
                print(f"Date : {tran_time}, Amount Credited : Rs.{transaction}, New Balance : {balance}")

print("Let's create an account first")
name = input("Enter your name : ")
person1 = Bank(name, 0)

ch = ''


while ch != 5:
    try:
        ch = int(input("1.Cash Deposit \n2.Cash Withdrawl \n3.Check Balance \n4.Statement \n5.Quit\n"))
        if ch == 1:
            n = int(input(f'Enter the Cash you want to deposit : Rs.'))
            person1.new_deposit(n)
        elif ch == 2:
            n = int(input('How much do you want to withdraw ? \nRs.'))
            person1.withdraw(n)
        elif ch == 3:
            person1.check_balance()
        elif ch == 4:
            person1.statement()
    except ValueError:
        print('Please enter the valid options!\n')

