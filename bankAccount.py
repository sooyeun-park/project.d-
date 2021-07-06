#! /usr/bin/env python
import sys
class Account:
    __balance = '0'
    d_account = {}

    def __init__(self, user_name, user_password):
        self.name = f'{self}'    
        self.__password = 'user_password'

    def deposit(self,amount): #입금
        r_deposit = (int(self.__balance)+ int(amount))
        self.__balance = r_deposit
        return self.__balance
    def withdraw(self,amount): #출금
        r_withdraw = (int(self.__balance)- int(amount))
        self.__balance = r_withdraw
        return self.__balance
    
    def transfer(self, who, amount): #송금
        self.__balance = int(self.__balance) - int(amount)
        who.__balance = int(who.__balance) + int(amount)
        
        
    def showBalance(self):
       print(self.__balance, '원')

soo= Account('soo', '0525')
yeun = Account('yeun','1114')
print(soo.name)
#print(soo.__password)
soo.deposit(35000)
soo.withdraw(5000)
soo.transfer(yeun,3000)
soo.showBalance()
yeun.showBalance()
