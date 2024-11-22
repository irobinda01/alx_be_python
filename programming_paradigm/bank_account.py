class BankAccount:
  def __init__(self, account_balance = 0):
    self.__account_balance = account_balance

  def deposit(self,amount):
    self.__account_balance = self.__account_balance + amount
  
  def withdraw(self,amount):
    if amount > 0 and self.__account_balance > amount:
      self.__account_balance = self.__account_balance - amount
      return True
    return False
  
  def display_balance(self):
    print(f"Current Balance: ${self.__account_balance:.2f}")
  