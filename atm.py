class ATM(object):
    def __init__(self, card_holder, card_no, pin, amount):
        self.card_holder = card_holder
        self.card_no = card_no
        self.pin = pin
        self.amount = amount

    def CashDeposit(self, card_no, pin):
        input_1 = int(input("Please enter the amount to be desposited: "))
        print("Rs.",input_1," has been added to your account")
        self.amount = input_1 + self.amount

    def CashWithDrawl(self, card_no, pin):
        input_2 = int(input("Please enter the amount to be taken: "))
        print("Rs.",input_2," has been deducted from your account")
        self.amount = self.amount - input_2

    def BalanceEnquiry(self, card_holder, card_no, pin):
        print(card_holder, "the money left in your account is: Rs.", self.amount)

Julie = ATM("Julie", 2837-9873-5475, 8768, 50000)
#Julie.CashDeposit(2837-9873-5475, 8768)

Tom = ATM("Tom", 7329-7477-5797, 2644, 100000)
Tom.CashWithDrawl(7329-7477-5797, 2644)
Tom.BalanceEnquiry("Tom", 7329-7477-5797, 2644)
