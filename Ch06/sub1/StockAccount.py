from Ch06.sub1.Account import Account

class StockAccount(Account) :

    def __init__(self, bank, id, name, balance, stock, amount,price):
        super().__init__(self,bank, id, name, balance)
        self.stock = stock
        self.amount = amount
        self.price = price

    def sell(self, amount, price):
        self._balance += self.amount*self.price

    def buy(self, amount, price):
        self._balance -= self.amount*self.price

    def show(self):
        print('-'*30)
        print('은행명:',self._bank)
        print('은행명:',self._id)
        print('은행명:',self._name)
        print('은행명:',self._balance)
        print('은행명:',self._stock)
        print('은행명:',self._bank)