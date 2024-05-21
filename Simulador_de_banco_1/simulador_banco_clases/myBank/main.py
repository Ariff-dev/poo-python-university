from Account import *

# Crear un diccionario para almacenar las cuentas con identificadores únicos
cuentas = {}

# Función para crear una nueva cuenta y almacenarla en el diccionario
def crear_cuenta(name, balance, password):
    cuenta_id = len(cuentas)  # Usar la longitud del diccionario como identificador único
    cuentas[cuenta_id] = Cuenta(name, balance, password)
    print(f'Se ha creado una nueva cuenta con ID {cuenta_id}')

# Función para acceder a los métodos de una cuenta específica por su ID
def operar_cuenta(cuenta_id, operation, *args):
    cuenta = cuentas.get(cuenta_id)
    if cuenta:
        method = getattr(cuenta, operation, None)
        if method:
            return method(*args)
        else:
            print('Operación no válida')
            return False
    else:
        print('Cuenta no encontrada')
        return False

# Ejemplo de uso
crear_cuenta('Juan', 500, 'password123')
crear_cuenta('María', 1000, 'contraseña456')

operar_cuenta(0, 'deposit', 200, 'password123')
operar_cuenta(1, 'withdraw', 300, 'contraseña456')
operar_cuenta(1, 'get_balance', 'contraseña456')