class Cuenta():
  #Crea un constructor 
  def __init__(self, nombre, saldo, password):
    self.name = nombre #Asigna a la variable name que recibe a la variable del constructor
    self.balance = float(saldo)  #Asigna a la variable balance que recibe a la variable del constructor
    self.password = password #Asigna a la variable password que recibe a la variable del constructor
# Define el metodo deposito
  def deposito(self, cantidad_a_depositar, password):
    #Validacion de la contrsena
    if password != self.password:
      print('Contraseña incorrecta')
      return None
    if cantidad_a_depositar < 0:
      print('No puedes depositar un monto negativo')
      return None

    self.balance = self.balance + cantidad_a_depositar
    return self.balance
#Define el metodo retiro
  def retiro(self, cantidad_a_retirar, password):
    if password != self.password:
      print('Contraseña incorrecta')
      return None
    if cantidad_a_retirar < 0:
      print('No puedes retirar un monto negativo')
      return None
    if cantidad_a_retirar > self.balance:
      print('Saldo insuficiente')
      return None

    self.balance = self.balance - cantidad_a_retirar
    return self.balance
# Define el metodo obtener_saldo
  def obtener_saldo(self, password):
    if password != self.password:
      print('Contraseña incorrecta')
      return None
    return self.balance

  # Added for debugging
  def show(self):
    print('       Nombre:', self.name)
    print('       Saldo:', self.balance)
    print('       Contraseña:', self.password)
    print()


# Crear una cuenta
mi_cuenta = Cuenta("Joe", 500, "soup")

# Mostrar información de la cuenta
mi_cuenta.show()

# Depositar en la cuenta
nuevo_saldo = mi_cuenta.deposito(100, "soup")
print("Nuevo saldo:", nuevo_saldo)

# Retirar de la cuenta
nuevo_saldo = mi_cuenta.retiro(50, "soup")
print("Nuevo saldo:", nuevo_saldo)

# Obtener el saldo de la cuenta
saldo_actual = mi_cuenta.obtener_saldo("soup")
print("Saldo actual:", saldo_actual)