# single, multiple and multilevel inheritance
#multilevel inheritance
class bank:
    def transaction(self):
        print("total transaction value ")

    def account_opening(self):
        print("This will show you your account open status")

    def deposite(self):
        print("this will show your deposited account")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("This wills show your transaction from HDFC to ICIC")

class icici(HDFC_bank):
        pass

i = icici()
i.hdfc_to_icici()
i.deposite()
i.account_opening()
