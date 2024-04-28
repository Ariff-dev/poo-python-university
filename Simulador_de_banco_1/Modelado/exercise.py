class Bank(): 
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def showBank(self, name):
        if name == self.name:
            print(name)
my_bank = Bank("BBVA", "Mexico")

my_bank.showBank("BBVA")