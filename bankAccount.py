#! /usr/bin/env python
import sys
class Account:
    balance = '0'
    password = '0000'
#    def __init__(self, passwd):
#        self.__password = int(passwd)
    d_account = {'soo':'0525', 'yeun':'1114'}
    
    def logIn(self,password):
        if self.password != 0000 :  
            print('please setting password')        
        #elif self in d_account : 
        else : 
            sys.exit()

    def deposit(self,amount): #입금
        #k = input("input password :")
        #self.logInself(k)
        r_deposit = (int(self.balance)+ int(amount))
        self.balance = r_deposit
        #return self.balace 
    
    def withdraw(self,amount): #출금
        #self.lonIn()
        r_withdraw = (int(self.balance)- int(amount))
        self.balance = r_withdraw
    
    def transfer(self, who, amount): #송금
        #self.lonIn()
        self.balance = int(self.balance) - int(amount)
        who.balance = int(who.balance) + int(amount)
        
    def showBalance(self):
       print(self.balance, '원')

soo = Account()
yeun = Account()
soo.deposit(5000)
soo.withdraw(300)
soo.transfer(yeun,2000)
soo.showBalance()
yeun.showBalance()
