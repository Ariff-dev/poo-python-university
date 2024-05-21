# Programa de prueba usando cuentas
# Versión 1, utilizando variables explícitas para cada objeto Cuenta
# Importar todo el código de la clase Cuenta desde el archivo Account.py
from Account import *

# Crear dos cuentas
objeto_CuentaDeJoe = Cuenta('Joe', 100, 'ContraseñaDeJoe')
print("Se ha creado una cuenta para Joe")

objeto_CuentaDeMary = Cuenta('Mary', 12345, 'ContraseñaDeMary')
print("Se ha creado una cuenta para Mary")

objeto_CuentaDeJoe.show()
objeto_CuentaDeMary.show()
print()

# Llamar a algunos métodos de las cuentas diferentes
print('Llamando a métodos de las dos cuentas...')
objeto_CuentaDeJoe.deposit(50, 'ContraseñaDeJoe')
objeto_CuentaDeMary.withdraw(345, 'ContraseñaDeMary')
objeto_CuentaDeMary.deposit(100, 'ContraseñaDeMary')

# Mostrar las cuentas
objeto_CuentaDeJoe.show()
objeto_CuentaDeMary.show()


# Crear otra cuenta con la información proporcionada por el usuario
nombreUsuario = input('¿Cuál es el nombre para la nueva cuenta de usuario? ')
saldoUsuario = int(input('¿Cuál es el saldo inicial para esta cuenta? '))
passUsuario = input('¿Cuál es la contraseña que deseas utilizar para esta cuenta? ')
objeto_CuentaNueva = Cuenta(nombreUsuario, saldoUsuario, passUsuario)

# Mostrar la nueva cuenta de usuario creada
objeto_CuentaNueva.show()

# Realicemos un depósito de 100 en la nueva cuenta
objeto_CuentaNueva.deposit(100, passUsuario)

saldoUsuario = objeto_CuentaNueva.getBalance(passUsuario)
print()
print('Después de depositar 100, el saldo del usuario es:', saldoUsuario)

# Mostrar la nueva cuenta de usuario
objeto_CuentaNueva.show()