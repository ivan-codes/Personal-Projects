import time

class Bank_Account:
    def __init__(self, money, deposit, withdraw):
        self.deposit = deposit
        self.withdraw = withdraw
        self.money = money
    def depositmoney(self):
        self.money += self.deposit
        print("Your new balance is: " + str(self.money))
    def withdrawmoney(self):
        self.money -= self.withdraw
        print("your new balance is: " + str(self.money))
    def checkmoney(self):
        print("Your available balance is: " + str(self.money))

money_input = input("How much money do you have in your bank account? ")
deposit_input = input("How much would you like to deposit? ")
withdraw_input = input("How much would you like to withdraw? ")
d1 = Bank_Account(int(money_input), int(deposit_input), int(withdraw_input))

