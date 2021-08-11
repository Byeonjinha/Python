class Account:
    def __init__(self, bank, id, name, balance):
        # 속성
        self.bank = bank
        self.id = id
        self.name = name
        self.balance = balance
    #기능
    def deposit(self, balance):
        self.balance = balance
    def withdraw(self, balance):
        self.balance = balance
    def show(self):
        print('---------------------------')
        print('은행명 : ', self.bank )
        print('계좌번호', self.id)
        print('입금주 : ', self.name )
        print('현재잔액 : ', self.balance)