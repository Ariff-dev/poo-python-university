# Non-OOP
# Bank 3
# Two accounts

#* Cuenta_1
nombre_cuenta_0 = ''
saldo_cuenta_0 = 0
contrasenia_cuenta_0 = ''

#* Cuenta_2
nombre_cuenta_1 = ''
saldo_cuenta_1 = 0
contrasenia_cuenta_1 = ''

#*Numero de Cuentas
nCuentas = 0


#* Funcion para crear nueva cuenta:
    #? Parametros :
        #numero_de_cuenta
        #nombre
        #saldo
        #contrasenia
def nueva_cuenta(numero_de_cuenta, nombre, saldo, contrasenia):
  
#* Llama las variables globales
  global nombre_cuenta_0, saldo_cuenta_0, contrasenia_cuenta_0 
  global nombre_cuenta_1, saldo_cuenta_1, contrasenia_cuenta_1

#* Si el numero de cuenta es igual a 0
  if numero_de_cuenta == 0:
    nombre_cuenta_0 = nombre # Asigna el nombre de la cuenta_1
    saldo_cuenta_0 = saldo #Asigna el saldo de la cuenta_1
    contrasenia_cuenta_0 = contrasenia  #Asigna la contrasenia de la cuenta_1

#* Si el numero de cuenta es igual a 1
  if numero_de_cuenta == 1:
    nombre_cuenta_1 = nombre # Asigna el nombre de la cuenta_2
    saldo_cuenta_1 = saldo # Asigna el saldo de la cuenta_2
    contrasenia_cuenta_1 = contrasenia #Asigna la crontrasenia de la cuenta_2


#* Funcion que muestra los datos:
    #?Datos:
        #Cuenta
        #nombre
        #saldo
        #contraseña
def show():
  
  #* Llama las variables globales
  global nombre_cuenta_0, saldo_cuenta_0, contrasenia_cuenta_0
  global nombre_cuenta_1, saldo_cuenta_1, contrasenia_cuenta_1 

  #*Si el nombre de la cuenta_1 es diferente de '' ---> Equivale a que tiene ya un nombre
  if nombre_cuenta_0 != '':

    #*Muestra la informacion de la cuenta_1
    print('Cuenta 0')
    print('       nombre', nombre_cuenta_0)
    print('       saldo:', saldo_cuenta_0)
    print('       contraseña:', contrasenia_cuenta_0)
    print()


  #*Si el nombre de la cuenta_2 es diferente de '' ---> Equivale a que tiene ya un nombre
  if nombre_cuenta_1 != '':
      
      #*Muestra la informacion de la cuenta_2
      print('Cuenta 1')
      print('       nombre', nombre_cuenta_1)
      print('       saldo:', saldo_cuenta_1)
      print('       contraseña:', contrasenia_cuenta_1)
      print()

#* Funcion que pide 2 parametros:
    #numero de cuenta 
    #contrasenia
    #? Retorna: El saldo de la cuenta seleccionada 
def getsaldo(numero_de_cuenta, contrasenia):
  
  #*Llama a las variables globales
  global nombre_cuenta_0, saldo_cuenta_0, contrasenia_cuenta_0 
  global nombre_cuenta_1, saldo_cuenta_1, contrasenia_cuenta_1

  #* Si el numero de cuenta == 0
  if numero_de_cuenta == 0:
      
      #*Si el //parametro// = contrasenia es difernte de la contrasenia de la cuenta_1
      if contrasenia != contrasenia_cuenta_0:
          
          #! Muestra error
          print('Contraseña incorrecta')
          return None
      
    #*Si el //parametro// = contrasenia es igual a la contrasenia de la cuenta_1
      #?Retorna el saldo de la cuenta_1
      return saldo_cuenta_0
  
  #* Si el numero de cuenta == 0
  if numero_de_cuenta == 1:
      
      #*Si el //parametro// = contrasenia es difernte de la contrasenia de la cuenta_2
      if contrasenia != contrasenia_cuenta_1:
          
           #! Muestra error
          print('Contraseña incorrecta')
          return None
      
      #*Si el //parametro// = contrasenia es igual a la contrasenia de la cuenta_2
      #?Retorna el saldo de la cuenta_2
      return saldo_cuenta_1
  

#  --- Recortamos las funciones adicionales deposito() y retiro() ---
#* Funcion de deposito 
  #? Retonar el saldo de la cuenta + el deposito solicitado
def deposito (numero_de_cuenta, deposito, contrasenia):
   #*Llamamos las variables globales
   global nombre_cuenta_0, saldo_cuenta_0, contrasenia_cuenta_0 
   global nombre_cuenta_1, saldo_cuenta_1, contrasenia_cuenta_1
   
   #* Si numero de cuenta == 0 entonces:
   if( numero_de_cuenta == 0):
      #* Validar si contrasenia es diferente de la contrasenia de la cuenta 0
      if( contrasenia != contrasenia_cuenta_0):
         #! Mostrar error
         return "Contrasenia Incorrecta"
      
    #*Crear el nuevo saldo usando el saldo de la cuenta_1 + el deposito 
      nuevo_saldo = saldo_cuenta_0 + deposito
      return f"Tu saldo actual es: ${nuevo_saldo}"
   

     #* Si numero de cuenta == 1 entonces:
   if( numero_de_cuenta == 1):
      #* Validar si contrasenia es diferente de la contrasenia de la cuenta 1
      if( contrasenia != contrasenia_cuenta_1):
         #! Mostrar error
         return "Contrasenia Incorrecta"
      
      #*Crear el nuevo saldo usando el saldo de la cuenta_1 + el deposito 
      nuevo_saldo = saldo_cuenta_1 + deposito
      return f"Tu saldo actual es: ${nuevo_saldo}"


#* Funcion de retiro que recibe 3 parametros 
    # Numero de cuenta
    # Monto de retiro
    # Contrasenia
def retiro(numero_de_cuenta,monto_de_retiro, contrasenia):
    #*Llamamos las variables globales
   global nombre_cuenta_0, saldo_cuenta_0, contrasenia_cuenta_0 
   global nombre_cuenta_1, saldo_cuenta_1, contrasenia_cuenta_1

   #*Validacion para numeros negativos en el monto
   if( monto_de_retiro < 0):
      return "No puedes agregar numeros negativos"      

    #* Si numero de cuenta == 0 entonces:
   if( numero_de_cuenta == 0): 
        #* Si la contrasenia es diferente de la cuenta_1
      if( contrasenia != contrasenia_cuenta_0):
         #! Mostrar error
         return "Contrasenia Incorrecta"
      
      #* Realizar la operacion del nuevo saldo
      nuevo_saldo = saldo_cuenta_0 - monto_de_retiro

      #* Si el nuevo saldo es menor de entonces
      if(nuevo_saldo < 0):
        #! Mostrar error
         return "No tienes suficientes fondos para realizar esta accion"
      return f"Tu saldo es: {nuevo_saldo}"
   
    #* Si numero de cuenta == 1 entonces:
   if( numero_de_cuenta == 1): 
        #* Si la contrasenia es diferente de la cuenta_1
      if( contrasenia != contrasenia_cuenta_1):
         #! Mostrar error
         return "Contrasenia Incorrecta"
      
       #* Realizar la operacion del nuevo saldo
      nuevo_saldo = saldo_cuenta_1 - monto_de_retiro
      #* Si el nuevo saldo es menor de entonces
      if(nuevo_saldo < 0):
        #! Mostrar error
         return "No tienes suficientes fondos para realizar esta accion"
      return f"Tu saldo es: {nuevo_saldo}"
      
#  --- Tambien el código principal que las llama ---

while True:
  print()
  print('Presiona b para obtener tu nueva cuenta') #f: nueva_cuenta()
  print('Presiona s para mostrar cuenta(s)') #f:show()
  print('Presiona d para hacer un deposito') #f:deposito()
  print('Presiona w para hacer un retiro') #f: retiro()
  print('Presiona a para hacer un retiro') #f: getsaldo()
  print('Presiona q para salir')
  print()

  action = input('¿Qué te gustaría hacer? ') 
  action = action.lower()  # forzamos las minúsculas
  print()

  def switchAction (action):
     if action == "b":
        global nCuentas 
        global nombre_cuenta_0, saldo_cuenta_0, contrasenia_cuenta_0
        global nombre_cuenta_1, saldo_cuenta_1, contrasenia_cuenta_1
        
        nCuentas = nCuentas + 1
        if( nCuentas == 0): 
           numero_de_cuenta = 0
           nombre = input("Escribe el nombre de la cuenta: ")
           saldo = 0
           contrasenia = input("Escribe la contraseña para la cuenta: ")
           return nueva_cuenta( numero_de_cuenta, nombre, saldo, contrasenia)
        if( nCuentas == 1):
           numero_de_cuenta: 1
           nombre = input("Escribe el nombre de la cuenta: ")
           saldo = 0
           contrasenia = input("Escribe la contraseña para la cuenta: ")
           return nueva_cuenta( numero_de_cuenta, nombre, saldo, contrasenia)
        else:
           return "No se pueden crear mas cuentas"
          
     elif action == "s":
        show();
     elif action == "d":

        numero_de_cuenta = input("¿En que cuenta quieres hacer el deposito?")

        if( numero_de_cuenta == 0):
           input_deposito = int(input("¿Cúanto quieres depositar?"))
           contrasenia = input("Escribe la contraseña de la cuenta: ")

           if( contrasenia != contrasenia_cuenta_0):
              return "Contraseña Incorrecta"
           
           deposito(numero_de_cuenta, input_deposito, contrasenia)

        if( numero_de_cuenta == 1):
           
           input_deposito = int(input("¿Cúanto quieres depositar?"))

           contrasenia = input("Escribe la contraseña de la cuenta: ")
           if( contrasenia != contrasenia_cuenta_1):
              return "Contraseña Incorrecta"
           
           deposito(numero_de_cuenta, input_deposito, contrasenia)
        else:
           return "Selecciona una cuenta existente"
          

     elif action == "w":
            numero_de_cuenta = input("¿En que cuenta quieres hacer el retiro?")

            if( numero_de_cuenta == 0):
                input_retirar = int(input("¿Cúanto quieres retirar?"))
                contrasenia = input("Escribe la contraseña de la cuenta: ")
                if( contrasenia != contrasenia_cuenta_0):
                    return "Contraseña Incorrecta"

                retiro(numero_de_cuenta, input_retirar, contrasenia)

            if( numero_de_cuenta == 1):
                input_retirar = int(input("¿Cúanto quieres retirar?"))
                contrasenia = input("Escribe la contraseña de la cuenta: ")
                if( contrasenia != contrasenia_cuenta_1):
                    return "Contraseña Incorrecta"
                
                retiro(numero_de_cuenta, input_retirar, contrasenia)
     elif action == "a": 
            numero_de_cuenta = input("¿En que cuenta quieres mostrar el saldo?")

            if( numero_de_cuenta == 0):
               contrasenia = input("Escribe la contraseña de la cuenta: ")
               if( contrasenia != contrasenia_cuenta_0):
                    return "Contraseña Incorrecta"
               getsaldo(numero_de_cuenta, contrasenia)
            
            if( numero_de_cuenta == 1):
               contrasenia = input("Escribe la contraseña de la cuenta: ")
               if( contrasenia != contrasenia_cuenta_1):
                    return "Contraseña Incorrecta"
               getsaldo(numero_de_cuenta, contrasenia)
     elif action == "q":
        return print('Bye')
     

  print(switchAction(action))
  print(action)
