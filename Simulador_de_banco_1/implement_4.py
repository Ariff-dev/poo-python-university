# Non-OOP Bank
# Version 4
# Any number of accounts - with lists

# Funciones: 
# - nueva_cuenta( )
# - show( )
# - getsaldo( )
# - deposito( )
# - retiro( )

# Definimos las listas que contendran los datos
lista_nombres_cuentas = [] 
lista_saldos_cuentas = [] 
lista_contrasenias_cuentas = []

def nueva_cuenta(nombre, saldo, contrasenia):
  #Se llaman  a las variables globales   
  global lista_nombres_cuentas, lista_saldos_cuentas, lista_contrasenias_cuentas
  lista_nombres_cuentas.append(nombre) 
  lista_saldos_cuentas.append(saldo) 
  lista_contrasenias_cuentas.append(contrasenia)

def show(numero_de_cuenta):
  global lista_nombres_cuentas, lista_saldos_cuentas, lista_contrasenias_cuentas
  print('       Cuenta', numero_de_cuenta)
  print('       nombre', lista_nombres_cuentas[numero_de_cuenta])
  print('       saldo:', lista_saldos_cuentas[numero_de_cuenta])
  print('       contraseña:',lista_contrasenias_cuentas[numero_de_cuenta])
  print()

def obtener_saldo(numero_de_cuenta, contrasenia):
  global lista_nombres_cuentas, lista_saldos_cuentas, lista_contrasenias_cuentas
  if contrasenia != lista_contrasenias_cuentas[numero_de_cuenta]:
    print('Contraseña incorrecta')
    return None
  return lista_saldos_cuentas[numero_de_cuenta]

def deposito(numero_de_cuenta, deposito, contrasenia):
    global lista_saldos_cuentas, lista_contrasenias_cuentas
    saldoActual = lista_saldos_cuentas[numero_de_cuenta]

    if( contrasenia != lista_contrasenias_cuentas[numero_de_cuenta]):
      print('Contraseña incorrecta')
      return None
    nuevo_saldo = saldoActual + deposito
    lista_saldos_cuentas[numero_de_cuenta] = nuevo_saldo
    print(f"Tu saldo es: {nuevo_saldo}")

def retiro(numero_de_cuenta, deposito, contrasenia):
    global lista_saldos_cuentas, lista_contrasenias_cuentas
    saldoActual = lista_saldos_cuentas[numero_de_cuenta]

    if( contrasenia != lista_contrasenias_cuentas[numero_de_cuenta]):
      print('Contraseña incorrecta')
      return None
    nuevo_saldo = saldoActual - deposito
    if( nuevo_saldo < 0):
      print("No tienes suficientes fondos para realizar esta accion")
      return None
    lista_saldos_cuentas[numero_de_cuenta] = nuevo_saldo
    print(f"Tu saldo es: {nuevo_saldo}")

#  --- Nos saltamos las demás funciones ---
# Creamos dos cuentas de prueba
  
print("La cuenta de Joe es la cuenta numero:", len(lista_nombres_cuentas)) 
nueva_cuenta("Joe", 100, 'soup')
print("La cuenta de Mary es la cuenta numero :", len(lista_nombres_cuentas)) 
nueva_cuenta("Mary", 12345, 'nuts')

while True:
  print()
  print('Presiona b para obtener tu saldo') 
  print('Presiona d para hacer un deposito')
  print('Presiona w para hacer un retiro') 
  print('Presiona s para mostrar la cuenta') 
  print('Presiona q para salir')
  print()
  action = input('¿Qué te gustaría hacer? ')
  action = action.lower()  # forzamos las minúsculas
  print()
  if action == 'b':
    print('Obtener saldo:')
    user_numero_de_cuenta = input('Por favor ingresa tu número de cuenta')
    user_numero_de_cuenta = int(user_numero_de_cuenta)
    user_contrasenia = input('Por favor ingresa la contrasenia: ')
    saldo = obtener_saldo(user_numero_de_cuenta, user_contrasenia)
    if saldo is not None:
      print('Your saldo is:', saldo)
  if action == 'd':
    number_account = int(input("¿En qué cuenta quieres hacer tu deposito?"))
    number_deposito = int(input("¿Cuánto quieres depositar?"))
    if(number_deposito < 0):
      print('Uitliza numeros positivos')
      break
    contrasenia = input("Escribe la contraseña de la cuenta: ")
    deposito(number_account,number_deposito, contrasenia)
  if action == 'w':
     number_account = int(input("¿En qué cuenta quieres hacer tu retiro?"))
     number_retirar = int(input("¿Cuánto quieres retirar?"))
     if(number_deposito < 0):
      print('Uitliza numeros positivos')
      break
     contrasenia = input("Escribe la contraseña de la cuenta: ")
     retiro(number_account,number_retirar, contrasenia)
  if action == 's':
    user_numero_de_cuenta = int(input('Por favor ingresa tu número de cuenta'))
    show(user_numero_de_cuenta)
  if action == 'q':
     break
#   --- Nos saltamos parte del código principal ---
   
print('Bye')