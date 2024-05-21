class Cuenta:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amount, password):
        if password != self.password:
            print('Contraseña incorrecta')
            return False
        self.balance += amount
        print(f'Se han depositado {amount} en la cuenta de {self.name}. Nuevo saldo: {self.balance}')
        return True

    def withdraw(self, amount, password):
        if password != self.password:
            print('Contraseña incorrecta')
            return False
        if amount > self.balance:
            print('Saldo insuficiente')
            return False
        self.balance -= amount
        print(f'Se han retirado {amount} de la cuenta de {self.name}. Nuevo saldo: {self.balance}')
        return True

    def get_balance(self, password):
        if password != self.password:
            print('Contraseña incorrecta')
            return False
        return self.balance