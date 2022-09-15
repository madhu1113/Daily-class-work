# single, multiple and multilevel inheritance
# multiple Inheritance

class bank:
    def transaction(self):
        print("total transaction value ")

    def account_opening(self):
        print("This will show you your account open status")

    def deposite(self):
        print("this will show your deposited account")

    def test(self):
        print("this is a test method from bank class")

class HDFC_bank:
    def hdfc_to_icici(self):
        print("This wills show your transaction from HDFC to ICIC")

    def test(self):
        print("this is a test method from HDFC_bank class")

class KLH_bank:
    def account_status_icici(self):
        print("print an account status in icici ")
#
# class icici(bank, HDFC_bank):  --> if we call test function then whichever class we have passed first first as argument those function will be executed.
#     pass

class icici(bank,HDFC_bank,KLH_bank): # if there is a conflict wrt name then it will consider the the function of first argument we pass as parameter.
    pass
i = icici()
i.hdfc_to_icici()
i.transaction()
i.deposite()
i.account_opening()
i.test()
i.account_status_icici()


# Concepts we will learn
# class
# object
# constructor
# inheritance
# private
# public
# protected
# abstraction
# encapsulation
# polymorphism
# package
# modules

