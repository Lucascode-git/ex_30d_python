from pprint import pprint
class PersonAccount:
  def __init__(self, firstname, lastname ):
    self.firstname = firstname
    self.lastname = lastname
    self.incomes = {}
    self.expenses = {}
  
  def add_income(self, amount, description):
    self.incomes[amount]=description  

  def add_expense(self, price, description):
    self.expenses[price]=description
    
  def total_income(self):
    return sum(self.incomes.keys())
  
  def total_expense(self):
    return sum(self.expenses.keys())

  def account_balance(self):
    return self.total_income() - self.total_expense()

  def account_info(self):
    return f'''\n=========== {self.firstname} {self.lastname} BALANCE: {self.account_balance()}€ ============\n
### Total income: ###\t{self.total_income()} € 
### Total expense: ###\t{self.total_expense()} €
\n======================================================
All incomes:
{self.incomes}
\nAll expenses:
{self.expenses}
======================================================\n'''


lm = PersonAccount('Lucas', 'MARIE')

lm.add_income(2000,'freelance')
lm.add_expense(1000,'loyer')
lm.add_income(1092, 'GAN')
lm.add_expense(89.65, 'food')
lm.add_expense(348.77,'shoes')

print(lm.account_info())